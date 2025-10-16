from threading import Thread
from order import Order, SUPPORTED_TEMPERATURES, ORDER_WASTED
from shelf import OVERFLOW_SHELF_NAME
import time


class OrderingThread(Thread):
    """
    Note that n order to control orders_per_second, this class is designed by
    running with 1 thread. In order to support multi-threading of this class,
    just need to protect "orders" in its own class with thread lock
    """
    def __init__(self, orders, orders_per_second, shelves, pickup_queue):
        Thread.__init__(self)
        self.orders, self.shelves, self.pickup_queue = orders, shelves, \
                                                       pickup_queue
        if orders_per_second <= 0:
            raise ValueError("Invalid orders_per_second value: {}"
                             .format(orders_per_second))
        self.delay = 1.0 / orders_per_second

    def __process_order(self, order):
        shelf = self.shelves[order.temperature]
        overflow_shelf = self.shelves[OVERFLOW_SHELF_NAME]
        # 1. add to regular temp shelf
        if shelf.add_order(order):
            print("> shelf {} has a new order {}\r\n{}".format(
                order.temperature, order, self.shelves))
            # now add the order for pickup queue
            self.pickup_queue.add_order(order)
            return
        # 2. add to overflow shelf
        elif overflow_shelf.add_order(order):
            print("> shelf {} has a new order {}\r\n{}".format(
                OVERFLOW_SHELF_NAME, order, self.shelves))
            # now add the order for pickup queue
            self.pickup_queue.add_order(order)
            return
        # 3. find if any available shelf with capacity, when we call
        # add_order() below, it may not have capacity anymore, that's ok
        avail_shelves = [shelf for shelf in self.shelves.values() if
                         shelf.temperature in SUPPORTED_TEMPERATURES and
                         shelf.has_capacity()]

        order_to_remove = None
        if avail_shelves:
            for item in overflow_shelf.orders.values():
                if order_to_remove:
                    break
                for shelf in avail_shelves:
                    if item.temperature == shelf.temperature:
                        if shelf.add_order(item):
                            # TODO: now the item exists in both the shelf and
                            #  overflow shelf at this moment, pick_up thread
                            #  could pick up from any of these 2 shelves
                            #  ideally need some type of transaction mechanism
                            # current solution is to mark order.picked_up =
                            # True after the order is picked up, so the orphan
                            # order will be cleaned up from the shelf based on
                            # this state
                            print("<> moved {} from overflow shelf to shelf {}"
                                  .format(item, shelf.temperature))
                            order_to_remove = item
                            break
        if order_to_remove: # found available shelf for this order,
            # let's remove it from  overflow
            ret = overflow_shelf.pickup_order(order_to_remove.id, moved=True)
            assert ret, "order {} failed to removed from " \
                        "overflow shelf".format(item)
            print(self.shelves)
        # 4. no available shelf found, let's dispose a random order
        else:
            waste_order = overflow_shelf.dispose_random_order()
            waste_order.order_state = ORDER_WASTED
            print(self.shelves)

        if overflow_shelf.add_order(order):
            print("> shelf {} has a new order {}\r\n{}".format(
                OVERFLOW_SHELF_NAME, order, self.shelves))
            # now add the order for pickup queue
            self.pickup_queue.add_order(order)
        else:
            raise Exception("order {} failed to be added "
                            "into overflow shelf".format(order))

    def run(self, dryrun=False):
        while(self.orders):
            order = self.orders.pop(0)
            self.__process_order(Order(order['id'], order['name'],
                                       order['temp'], order['shelfLife'],
                                       order['decayRate']))
            if not dryrun:
                time.sleep(self.delay)
        self.pickup_queue.end_ordering()
