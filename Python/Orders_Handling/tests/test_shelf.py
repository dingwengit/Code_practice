from testbase import OrderTestCase
from shelf import Shelf, CAPACITY
from uuid import uuid4
from order import ORDER_PICKEDUP


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

        # test clean up order
        self.add_orders_to_capacity(shelf1)
        shelf1.orders.values()[0].order_state = ORDER_PICKEDUP
        removed = shelf1.cleanup_orders()
        self.assertEqual(True, removed)
        self.assertEqual(len(shelf1.orders), CAPACITY - 1)

        shelf1.orders.values()[0].order_time -= 1000
        removed = shelf1.cleanup_orders()
        self.assertEqual(True, removed)
        self.assertEqual(len(shelf1.orders), CAPACITY - 2)

    def negative_tests(self):
        shelf1 = Shelf('hot')
        # over capacity
        self.add_orders_to_capacity(shelf1)
        extra_order_added = shelf1.add_order(self.generate_order())
        self.assertFalse(extra_order_added)

        # pickup order (non exist)
        pickup_order = shelf1.pickup_order(str(uuid4()))
        self.assertEqual(None, pickup_order)

        # test has_capacity
        has_capacity = shelf1.has_capacity()
        self.assertFalse(has_capacity)

