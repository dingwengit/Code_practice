from unittest import TestCase
from order import Order, SUPPORTED_TEMPERATURES
from shelf import CAPACITY
from uuid import uuid4


class OrderTestCase(TestCase):
    """
    base test class for common test function
    """
    @staticmethod
    def generate_order():
        order1 = {"id": str(uuid4()),
                  "name": "Cheese Pizza",
                  "temp": SUPPORTED_TEMPERATURES[0],
                  "shelfLife": 300,
                  "decayRate": 0.45}
        new_order = Order(order1['id'], order1['name'], order1['temp'],
                          order1['shelfLife'], order1['decayRate'])
        return new_order

    @staticmethod
    def add_orders_to_capacity(shelf1, capacity=CAPACITY):
        for _ in range(capacity):
            shelf1.add_order(OrderTestCase.generate_order())
