#!/usr/bin/python

import argparse
from kitchen import Kitchen

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-of","--orders_file", help="order json file",
                        required=True)
arg_parser.add_argument("-op", "--orders_per_second",
                        help="how many orders per second to send to kitchen, default is 2")
args = arg_parser.parse_args()
ORDERS_PER_SECOND = 2


if __name__ == '__main__':
    orders_per_second = ORDERS_PER_SECOND
    if args.orders_per_second:
        orders_per_second = float(args.orders_per_second)
    Kitchen(args.orders_file, orders_per_second).start()
