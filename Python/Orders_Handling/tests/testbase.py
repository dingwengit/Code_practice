from unittest import TestCase
from order import Order
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
                  "temp": "hot",
                  "shelfLife": 300,
                  "decayRate": 0.45}
        new_order = Order(order1['id'], order1['name'], order1['temp'],
                          order1['shelfLife'], order1['decayRate'])
        return new_order

    @staticmethod
    def add_orders_to_capacity(shelf1, capacity=CAPACITY):
        orders = []
        for _ in range(capacity):
            orders.append(OrderTestCase.generate_order())
        map(shelf1.add_order, orders)
