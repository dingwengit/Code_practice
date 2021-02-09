from threading import Thread
from order import Order
from shelf import OVERFLOW_SHELF_NAME
import time

THREAD_DELAY_SECONDS = 3


class PickupThread(Thread):
    def __init__(self, pickup_queue, shelves):
        Thread.__init__(self)
        self.pickup_queue = pickup_queue
        self.shelves = shelves

    def __pickup_order(self, order: Order):
        shelf = self.shelves[order.temperature]
        overflow_shelf = self.shelves[OVERFLOW_SHELF_NAME]
        if shelf.pickup_order(order.id):
            print(self.shelves)
            return
        elif overflow_shelf.pickup_order(order.id):
            print(self.shelves)
            return

    def run(self):
        while(not self.pickup_queue.end_pickup_thread()):
            order = self.pickup_queue.pickup_order()
            if not order:
                continue
            self.__pickup_order(order)
            time.sleep(THREAD_DELAY_SECONDS)
