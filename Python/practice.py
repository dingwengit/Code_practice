"""

()a()(()()
->

incoming events schema:

location_id, device_id, timestamp (epoch time), blocked_event_type, blocked_site
loc_001,     dev_001,   572315765, ad,   googleanalytics.com
loc_002,     dev_002,   572315767, kids, marijuana.com
loc_003,     dev_003,   572315793, spam, nigerianprince.com
----

how to process S3 files -->
(1) Kalfka data source --> Kalfka event
(2) log reader --> monitor files --> process it


1. calculate and display week over week cumulative counts by blocked_event_type

      week 1,  week 2,   week 3, ...
ad    38479,   52215,   98234,
kids  2834,    6255,    8217

2. output (daily, weekly)

daily workflow --> input as stream

day1.psv --> type, count_events
day2.psv --> type, count_events
day3.psv --> type, count_events

(1) weekly workflow --> input as daily output files
(2) SQL query
(3) kafka events --> send out topics for daily count by type
"""
