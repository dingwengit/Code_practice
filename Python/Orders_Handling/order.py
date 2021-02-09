import time
import re

# allowed temperatures of orders, also means that only these shelves are
# supported in the kitchen
SUPPORTED_TEMPERATURES = ["hot", "cold", "frozen"]

# valid range for shelf life for an order in seconds as (min, max)
SHELF_LIFE_RANGE = (1, 24 * 60 * 60)
# valid range for order decay rate as (min, max)
DECAY_RATE_RANGE = (0, 1)
# valid range for decay modifier as (min, max)
DECAY_MODIFIER_RANGE = (1, 100)


class Order():
    """
    Order class
    """
    def __init__(self, id, name, temperature, shelfLife, decayRate):
        """
        :param id: order id
        :param name: name of the order
        :param temperature: Preferred shelf storage temperature
        :param shelfLife: Shelf wait max duration (seconds)
        :param decayRate: Value deterioration modifier
        """
        self.__validate_order_id(id)
        self.__check_range(shelfLife, SHELF_LIFE_RANGE)
        self.__check_range(decayRate, DECAY_RATE_RANGE)
        if temperature not in SUPPORTED_TEMPERATURES:
            raise ValueError("{} is not in supported temperature list {}"
                             .format(temperature, SUPPORTED_TEMPERATURES))
        self.id, self.name, self.temperature, self.shelfLife, self.decayRate\
            = id, name, temperature, shelfLife, decayRate
        self.order_time = time.time()
        self.shelfDecayModifier = 1
        self.order_value = 1
        self.picked_up = False

    def __repr__(self):
        return "id:{}, name:{}, temp:{}, shelfLife:{}, decayRate:{}, " \
               "pickedup: {}, cur_value:{:.2f}"\
            .format(self.id, self.name, self.temperature, self.shelfLife,
                    self.decayRate, self.picked_up, self.get_value())

    @staticmethod
    def __check_range(value, range):
        if not range[1] >= value >= range[0]:
            raise ValueError("{} is not in valid range of {}"
                             .format(value, range))

    @staticmethod
    def __validate_order_id(order_id):
        exp = ('^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}'
               '-[0-9a-f]{4}-[0-9a-f]{12}$')
        if not re.match(exp, order_id):
            raise ValueError("Invalid order id format {}".format(order_id))

    def set_shelf_decay_modifier(self, value):
        """
        :param value: update shelfDecayModifier
        :return:
        """
        self.__check_range(value, DECAY_MODIFIER_RANGE)
        self.shelfDecayModifier = value

    def get_value(self):
        if self.order_value == 0:
            return self.order_value
        order_age = int(time.time() - self.order_time)
        value = self.shelfLife - self.decayRate * order_age * \
                self.shelfDecayModifier
        if int(value) < 0:
            self.order_value = 0
        else:
            self.order_value = value / self.shelfLife
        return self.order_value
