import json
from order_thread import OrderingThread
from pickup_thread import PickupThread
from cleanup_thread import CleanupThread
from order import Order, SUPPORTED_TEMPERATURES
from shelf import Shelf, OVERFLOW_SHELF_NAME
from pickup import PickupQueue

PICKUP_THREADS = 1


class Kitchen():
    def __init__(self, order_file, orders_per_second):
        self.orders = self.__read_orders(order_file)
        self.orders_per_second = orders_per_second
        self.shelves = dict()
        self.__create_shelves()

    def __create_shelves(self):
        for temp in SUPPORTED_TEMPERATURES:
            self.shelves[temp] = Shelf(temp)
        assert OVERFLOW_SHELF_NAME not in self.shelves, \
            "{} already exists in supported shelves {}"\
                .format(OVERFLOW_SHELF_NAME, SUPPORTED_TEMPERATURES)
        self.shelves[OVERFLOW_SHELF_NAME] = Shelf(OVERFLOW_SHELF_NAME, True)

    @staticmethod
    def __read_orders(order_file):
        with open(order_file) as f:
            orders = json.load(f)
        return orders

    def start(self):
        pickup_queue = PickupQueue()
        order_thread = OrderingThread(self.orders, self.orders_per_second,
                                      self.shelves, pickup_queue)
        cleanup_thread = CleanupThread(self.shelves, pickup_queue)
        threads = [order_thread, cleanup_thread]
        for _ in range(PICKUP_THREADS):
            threads.append(PickupThread(pickup_queue, self.shelves))
        for t in threads:
            t.start()
        # Wait for all threads to complete
        for t in threads:
            t.join()
        print("Exiting Main Thread")