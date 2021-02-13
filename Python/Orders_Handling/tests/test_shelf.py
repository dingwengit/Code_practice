from testbase import OrderTestCase
from shelf import Shelf, CAPACITY
from uuid import uuid4
from order import ORDER_PICKEDUP, SUPPORTED_TEMPERATURES


class ShelfTest(OrderTestCase):
    """
    Unit test for Shelf class
    for all public class methods, perform postive and negative tests
    """
    def positive_tests(self):
        # test add_order
        new_order = self.generate_order()
        shelf1 = Shelf(new_order.temperature)
        order_added = shelf1.add_order(new_order)
        self.assertTrue(order_added)

        # test pickup_order
        pickup_order = shelf1.pickup_order(new_order.id)
        self.assertEqual(new_order, pickup_order)

        # test has_capacity
        has_capacity = shelf1.has_capacity()
        self.assertTrue(has_capacity)

        # test dispose random order
        shelf1.add_order(new_order)
        waste_order = shelf1.dispose_random_order()
        self.assertEqual(new_order, waste_order)
        self.assertEqual(0, len(shelf1.orders))

        # test clean up order
        OrderTestCase.add_orders_to_capacity(shelf1)
        self.assertEqual(CAPACITY, len(shelf1.orders))
        list(shelf1.orders.values())[0].order_state = ORDER_PICKEDUP
        removed = shelf1.cleanup_orders()
        self.assertEqual(True, removed)
        self.assertEqual(CAPACITY - 1, len(shelf1.orders))

        list(shelf1.orders.values())[0].order_time -= 1000
        removed = shelf1.cleanup_orders()
        self.assertEqual(True, removed)
        self.assertEqual(CAPACITY - 2, len(shelf1.orders))

    def negative_tests(self):
        shelf1 = Shelf(SUPPORTED_TEMPERATURES[0])
        # over capacity
        OrderTestCase.add_orders_to_capacity(shelf1)
        extra_order_added = shelf1.add_order(self.generate_order())
        self.assertFalse(extra_order_added)

        # pickup order (non exist)
        pickup_order = shelf1.pickup_order(str(uuid4()))
        self.assertEqual(None, pickup_order)

        # test has_capacity
        has_capacity = shelf1.has_capacity()
        self.assertFalse(has_capacity)

