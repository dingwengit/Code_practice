from testbase import OrderTestCase
from pickup import PickupQueue


class PickupTest(OrderTestCase):
    """
    Unit test for Pickup class
    for all public class methods, perform postive and negative tests
    """
    def positive_tests(self):
        # test add_order
        new_order = self.generate_order()
        new_order.order_time -= 7
        pickup_queue = PickupQueue()
        pickup_queue.add_order(new_order)
        self.assertEqual(1, len(pickup_queue.queue))

        # test pick up order
        pickup_order = pickup_queue.pickup_order()
        self.assertIsNotNone(pickup_order)
        self.assertEqual(0, len(pickup_queue.queue))
        # cannot pickup the same order twice
        pickup_order = pickup_queue.pickup_order()
        self.assertIsNone(pickup_order)

        # test end pick up thread
        pickup_queue.end_ordering()
        self.assertEqual(True, pickup_queue.end_pickup_thread())

    def negative_tests(self):
        # test pick up an order that just received
        new_order = self.generate_order()
        pickup_queue = PickupQueue()
        pickup_queue.add_order(new_order)
        self.assertEqual(1, len(pickup_queue.queue))

        pickup_order = pickup_queue.pickup_order()
        self.assertIsNone(pickup_order)
        self.assertEqual(1, len(pickup_queue.queue))

        # test pickup orders in FIFO
        pickup_queue = PickupQueue()
        order1 = self.generate_order()
        order1.order_time -= 7
        pickup_queue.add_order(order1)
        order2 = self.generate_order()
        order2.order_time -= 7
        pickup_queue.add_order(order2)
        pickup_order = pickup_queue.pickup_order()
        self.assertNotEqual(pickup_order.id, order2.id)
        self.assertEqual(pickup_order.id, order1.id)


