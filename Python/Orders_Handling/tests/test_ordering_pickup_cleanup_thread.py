from testbase import OrderTestCase
from order_thread import OrderingThread
from order import SUPPORTED_TEMPERATURES, ORDER_WASTED, ORDER_PICKEDUP, \
    ORDER_RECEIVED
from shelf import Shelf, OVERFLOW_SHELF_NAME, CAPACITY, OVERFLOW_CAPACITY
from pickup import PickupQueue
from cleanup_thread import CleanupThread
from pickup_thread import PickupThread


class KitchenThreadTest(OrderTestCase):
    """
    Unit test for ordering, cleanup and pickup thread class
    for all public class methods, perform postive and negative tests
    """
    def __create_shelves(self, shelves):
        for temp in SUPPORTED_TEMPERATURES:
            shelves[temp] = Shelf(temp)
        shelves[OVERFLOW_SHELF_NAME] = Shelf(OVERFLOW_SHELF_NAME, True)

    def __create_orders(self, capacity):
        for _ in range(capacity):
            new_order = self.generate_order()
            self.temperature = new_order.temperature
            self.orders.append(
                {"id": new_order.id,
                 "name": new_order.name,
                 "temp": new_order.temperature,
                 "shelfLife": new_order.shelfLife,
                 "decayRate": new_order.decayRate}
            )

    def __setup(self):
        # setup orders and shelves
        self.shelves, self.orders = dict(), []
        self.__create_shelves(self.shelves)
        self.__create_orders(CAPACITY)
        orders_per_second, self.pickup_queue = 1, PickupQueue()
        self.ordering_thread = OrderingThread(self.orders, orders_per_second,
                                              self.shelves, self.pickup_queue)

    def order_thread_tests(self):
        self.__setup()

        # orders are put into its shelf and reach its capacity
        self.ordering_thread.run(dryrun=True)
        shelf1 = self.shelves[self.temperature]
        self.assertEqual(CAPACITY, len(shelf1.orders))
        shelf_overflow = self.shelves[OVERFLOW_SHELF_NAME]
        self.assertEqual(0, len(shelf_overflow.orders))

        # add one more order, it should go to overflow shelf
        new_order = self.generate_order()
        self.orders.append(
            {"id": new_order.id,
             "name": new_order.name,
             "temp": new_order.temperature,
             "shelfLife": new_order.shelfLife,
             "decayRate": new_order.decayRate}
        )
        self.ordering_thread.run(dryrun=True)
        self.assertEqual(CAPACITY, len(shelf1.orders))
        self.assertEqual(1, len(shelf_overflow.orders))

        # overflow test -
        # add another 15 orders, one order should be disposed as waste from
        # overflow shelf, so only 1 order in pickup_queue will have order
        # with waste state
        self.__create_orders(OVERFLOW_CAPACITY)
        self.ordering_thread.run(dryrun=True)
        self.assertEqual(CAPACITY, len(shelf1.orders))
        self.assertEqual(OVERFLOW_CAPACITY, len(shelf_overflow.orders))
        wasted_orders = 0
        for order in self.pickup_queue.queue:
            if order.order_state == ORDER_WASTED:
                wasted_orders += 1
        self.assertEqual(1, wasted_orders)

        # overflow test -
        # now change one order temperature in overflow shelf to another
        # temperature (other than 'hot', e.g., frozen) where its shelf has
        # capacity
        # then add another order 'hot' into orders, run order_thread,
        # now the 'frozen' order will be moved from overflow shelf into
        # 'frozen' shelf and overflow shelf still at its capacity
        new_temperature = 'frozen'
        this_order = list(shelf_overflow.orders.values())[0]
        this_order.temperature = new_temperature
        shelf_frozen = self.shelves[new_temperature]
        self.assertEqual(0, len(shelf_frozen.orders))
        new_order = self.generate_order()
        self.orders.append(
            {"id": new_order.id,
             "name": new_order.name,
             "temp": new_order.temperature,
             "shelfLife": new_order.shelfLife,
             "decayRate": new_order.decayRate}
        )
        self.ordering_thread.run(dryrun=True)
        self.assertEqual(1, len(shelf_frozen.orders))
        self.assertEqual(this_order, list(shelf_frozen.orders.values())[0])
        self.assertEqual(OVERFLOW_CAPACITY, len(shelf_overflow.orders))

    def cleanup_thread_tests(self):
        self.__setup()

        # test orders are put into it shelf and reach its capacity
        self.ordering_thread.run(dryrun=True)
        shelf1 = self.shelves[self.temperature]
        self.assertEqual(CAPACITY, len(shelf1.orders))
        cleanup_thread = CleanupThread(self.shelves, self.pickup_queue)

        # mark one onder's value as 0, and run clean up thread
        # the order should be marked as wasted, and remove from the shelf
        this_order = list(shelf1.orders.values())[0]
        this_order.order_time -= 1000
        cleanup_thread.run(dryrun=True)
        self.assertEqual(ORDER_WASTED, this_order.order_state)
        self.assertEqual(CAPACITY - 1, len(shelf1.orders))

    def pickup_thread_tests(self):
        self.__setup()

        # test orders are put into it shelf and reach its capacity
        self.ordering_thread.run(dryrun=True)
        shelf1 = self.shelves[self.temperature]
        self.assertEqual(CAPACITY, len(shelf1.orders))
        pickup_thread = PickupThread(self.pickup_queue, self.shelves)

        # mark order time to be ready for pickup, and run pick up thread
        # the first-in order should be marked as picked up, and remove from
        # the shelf
        this_order = self.pickup_queue.queue[0]
        this_order.order_time -= 7
        self.assertEqual(ORDER_RECEIVED, this_order.order_state)
        pickup_thread.run(dryrun=True)
        self.assertEqual(ORDER_PICKEDUP, this_order.order_state)
        self.assertEqual(CAPACITY - 1, len(shelf1.orders))


