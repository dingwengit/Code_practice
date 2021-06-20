###SQL 10 min
Table: block_events

---------------------+---------
Column
Name | Data
Type
reported_at | string
location_id | string
node_id | string
mac(device_id) | string
action | string
blocked_address | string
blocked_address_type | string
policy | string
category_id | array[int]
source | string
--------------------------------

Table: device_type

---------------------+---------
Column
Name | Data
Type
device_id | string
device_type | string
device_category | string
device_brand | string
--------------------------------

Table: user_security_override
---------------------+---------
Column
Name | Data
Type
location_id | string
device_id | string
whitelisted_address | string
created_at | string
source | string
policy | string
--------------------------------

## 1.Write a SQL query to calculate the following:

## a.How do you check which device id has multiple device type?
## b.Create a dummy variable to flag if a device has a device_type or not.

id1, type1, cat1, brand1
id2, type2, cat1, brand1

select
device_id
from device_type_tbl

group
by
device_id
having
count(device_type) > 1

select
ISNULL(device_type, "no device type"), *
from device_type_tbl

## c.Top 3 “blocked_address” for laptop devices within each policy(
# SpamPhish, Adblocking, Kids, Teens, AdultSensitive) in the last 7 days.

select
count(blocked_address), dt.device_type, policy in [xxx],
from block_events as be

join
device_type as dt
on
be.mac == dt.device_id
group
on
blocked_address
where
dt.device_type = "Laptop"