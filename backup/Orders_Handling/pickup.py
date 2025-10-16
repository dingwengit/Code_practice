from threading import Lock
from order import Order
from random import randint
import time

PICKUP_TIME_RANGE_SECONDS = (2, 6)


class PickupQueue():
    def __init__(self):
        self.lock = Lock()
        self.queue = []
        # this is to coordinate threads exit
        self.no_more_orders = False

    def add_order(self, order):
        with self.lock:
            assert order not in self.queue, \
                "order {} already exists in the pickup queue".format(order)
            self.queue.append(order)

    def pickup_order(self):
        with self.lock:
            pickup_idx, pickup_order = None, None
            for idx, order in enumerate(self.queue):
                # if it is ready to pick up
                duration = int(time.time() - order.order_time)
                if duration < PICKUP_TIME_RANGE_SECONDS[0]:
                    # the first order is not ready for pick up yet, skip the
                    # others
                    return None
                if duration > randint(PICKUP_TIME_RANGE_SECONDS[0],
                                      PICKUP_TIME_RANGE_SECONDS[1]):
                    pickup_idx, pickup_order = idx, order
                    break
            if pickup_idx is not None:
                del self.queue[pickup_idx]
            return pickup_order

    def end_ordering(self):
        self.no_more_orders = True

    def end_pickup_thread(self):
        return self.no_more_orders and not self.queue
