
from functools import wraps
import requests
from requests.exceptions import ConnectionError, Timeout
import time
import datetime
import json

# view angle from a office coordinate - +/- 15 degress on lattitude and
# longitude
DEFAULT_VIEW_ANGLE = 10
MAX_VIEW_ANGLE = 90
NIN_VIEW_ANGLE = 0
MAX_LANTITUDE = 90
MIN_LANTITUDE = -90
MAX_LONGITUDE = 180
MIN_LONGITUDE = -180


class Latitude():
    def __init__(self, value, direction):
        if value < 0 or value > MAX_LANTITUDE:
            raise ValueError("latitude {} is out of range(0, {})".format(
                value, MAX_LANTITUDE))
        directions = ['N', 'S']
        if direction not in directions:
            raise ValueError("direction {} is invalid, should be one of {} "
                .format(value, directions))
        self.value = -1 * value if direction == 'S' else value


class Longitude():
    def __init__(self, value, direction):
        if value < 0 or value > MAX_LONGITUDE:
            raise ValueError("longitude {} is out of range(0, {}})".format(
                value, MAX_LONGITUDE))
        directions = ['E', 'W']
        if direction not in directions:
            raise ValueError("direction {} is invalid, should be one of {} "
                .format(value, directions))
        self.value = -1 * value if direction == 'W' else value


class LocationViewBox():
    def __init__(self, latitude, longitude, view_angle=DEFAULT_VIEW_ANGLE):
        if view_angle < NIN_VIEW_ANGLE or view_angle > MAX_VIEW_ANGLE:
            raise ValueError("view_angle {} is out of range({}, {}})".format(
                view_angle, NIN_VIEW_ANGLE, MAX_VIEW_ANGLE))
        if not isinstance(latitude, Latitude):
            raise ValueError("latitude {} is not a Lattitude class "
                             "instance".format(latitude))
        if not isinstance(longitude, Longitude):
            raise ValueError("longitude {} is not a Longitude class "
                             "instance".format(longitude))
        # if the latitude change cross the north-pole or south pole,
        # use MAX_LANTITUDE or MIN_LANTITUDE
        # which means we don't allow latitude change over north pole
        self.ne_latitude = latitude.value + view_angle
        if self.ne_latitude > MAX_LANTITUDE:
            print("view angle is crossing north-pole")
            self.ne_latitude = MAX_LANTITUDE
        self.sw_latitude = latitude.value - view_angle
        if  self.sw_latitude < MIN_LANTITUDE:
            print("view angle is crossing south-pole")
            self.sw_latitude = MIN_LANTITUDE
        self.sw_longitude = longitude.value - view_angle
        if self.sw_longitude < MIN_LONGITUDE:
            self.sw_longitude = MAX_LONGITUDE + self.sw_longitude - \
                                MIN_LONGITUDE
        self.ne_longitude = longitude.value + view_angle
        if self.ne_longitude > MAX_LONGITUDE:
            self.ne_longitude = MIN_LONGITUDE + self.ne_longitude - \
                                MAX_LONGITUDE
        # print("{} {} {} {}".format(self.ne_latitude, self.sw_latitude,
        #                              self.sw_longitude, self.ne_longitude))

    def is_visible(self, latitude, longitude):
        latitude_visible, longitude_visible = False, False

        if not isinstance(latitude, Latitude):
            raise ValueError("latitude {} is not a Lattitude class "
                             "instance".format(latitude))
        if not isinstance(longitude, Longitude):
            raise ValueError("longitude {} is not a Longitude class "
                             "instance".format(longitude))

        if self.ne_latitude >= latitude.value >= self.sw_latitude:
            latitude_visible = True

        if self.sw_longitude < self.ne_longitude:
            if self.ne_longitude >= longitude.value >= self.sw_longitude:
                longitude_visible = True
        else:
            if self.ne_longitude >= longitude.value >= MIN_LONGITUDE or \
                longitude.value >= self.sw_longitude :
                longitude_visible = True
        return latitude_visible and longitude_visible


def retry(exceptions, tries=3, delay=5, backoff=2):
    def deco_retry(f):
        @wraps(f)
        def f_retry(*args, **kwargs):
            nextretry, nextdelay = tries, delay
            while nextretry > 0:
                try:
                    return f(*args, **kwargs)
                except exceptions as e:
                    msg = "Retrying in {} seconds because of '{}' " \
                          "...".format(nextdelay, e)
                    print(msg)
                    time.sleep(nextdelay)
                    nextretry -= 1
                    nextdelay *= backoff
            return f(*args, **kwargs)

        return f_retry

    return deco_retry


@retry((ConnectionError, Timeout), tries=3, delay=30)
def get_json_http(url):
    r = requests.get(url, timeout=600, verify=True)  # 10 min
    if r.status_code >= 500 and r.status_code < 600:
        raise ConnectionError("connection error due to gateway for {}"
                              .format(url))
    if r.status_code != 200:
        raise Exception("Got error code {} response from {}"
                        .format(r.status_code, url))
    return json.loads(r.text)


def get_nasa_data(start_date, end_date):
    datetime.datetime.strptime(start_date, '%Y-%m-%d')
    datetime.datetime.strptime(end_date, '%Y-%m-%d')
    url = "https://ssd-api.jpl.nasa.gov/fireball.api?date-min={}&date-max={}" \
          "&sort=-energy&req-loc=true".format(start_date, end_date)
    data = get_json_http(url)
    result = []
    energy_idx = data['fields'].index('energy')
    lat_idx = data['fields'].index('lat')
    lat_dir_idx = data['fields'].index('lat-dir')
    lon_idx = data['fields'].index('lon')
    lon_dir_idx = data['fields'].index('lon-dir')
    for item in data['data']:
        energy = float(item[energy_idx])
        latitude = Latitude(float(item[lat_idx]), item[lat_dir_idx])
        longitude = Longitude(float(item[lon_idx]), item[lon_dir_idx])
        result.append((energy, latitude, longitude))
    return result


def get_max_energy_obj(data, *args):
    ret = None
    max_engergy = 0
    for office in args:
        loc_view = LocationViewBox(
            Latitude(office['latitude'], office['latitude_direction']),
            Longitude(office['longitude'], office['longitude_direction']))
        for item in data:
            if loc_view.is_visible(item[1], item[2]):
                if ret is None or max_engergy < item[0]:
                    max_engergy = item[0]
                    ret = "office \"{}\" has the brightest star with " \
                          "object's energy {}, lat {} lon {}"\
                        .format(office['name'], item[0], item[1].value,
                                item[2].value)
                # because the data is sorted by energy, we only need the
                # first object
                break
    return ret


def fireball():
    start_date = "2017-01-01"
    end_date = "2020-01-01"
    office1 = {"name": "Boston", "latitude": 42.354558,
               "latitude_direction": "N", "longitude": 71.054254,
               "longitude_direction": "W"}
    office2 = {"name": "NCR", "latitude": 28.574389,
               "latitude_direction": "N", "longitude": 77.312638,
               "longitude_direction": "E"}
    office3 = {"name": "San Francisco", "latitude": 37.793700,
               "latitude_direction": "N", "longitude": 122.403906,
               "longitude_direction": "W"}
    data = get_nasa_data(start_date, end_date)
    print(get_max_energy_obj(data, office1, office2, office3))


def unit_tests():
    i = 1
    loc = LocationViewBox(Latitude(5, 'N'), Longitude(175.38, 'E'))
    if loc.is_visible(Latitude(10, 'S'), Longitude(170.38, 'W')):
        print("test {} pass".format(i))
    else:
        print("test {} failed".format(i))
    i += 1
    loc = LocationViewBox(Latitude(42.354558, 'N'), Longitude(71.054254, 'W'))
    if not loc.is_visible(Latitude(56.9, 'N'), Longitude(172.4, 'E')):
        print("test {} pass".format(i))
    else:
        print("test {} failed".format(i))


if __name__ == '__main__':
    unit_tests()
    fireball()