from unittest import TestCase
from order import Order


class OrderTest(TestCase):
    def positive_tests(self):
        order1 = { "id": "0ff534a7-a7c4-48ad-b6ec-7632e36af950",
                  "name": "Cheese Pizza",
                  "temp": "hot",
                  "shelfLife": 300,
                  "decayRate": 0.45}
        new_order = Order(order1['id'], order1['name'], order1['temp'],
                          order1['shelfLife'], order1['decayRate'])
        self.assertIsInstance(new_order, Order)

    def negative_tests(self):
        # invliad temperature
        order2 = { "id": "0ff534a7-a7c4-48ad-b6ec-7632e36af950",
                  "name": "Cheese Pizza",
                  "temp": "very hot",
                  "shelfLife": 300,
                  "decayRate": 0.45}
        try:
            new_order = Order(order2['id'], order2['name'], order2['temp'],
                              order2['shelfLife'], order2['decayRate'])
            self.assertIsNone(new_order)
        except Exception as ex:
            self.assertIsInstance(ex, ValueError)

        # invliad shelfLife
        order2 = { "id": "0ff534a7-a7c4-48ad-b6ec-7632e36af950",
                  "name": "Cheese Pizza",
                  "temp": "hot",
                  "shelfLife": 0,
                  "decayRate": 0.45}
        try:
            new_order = Order(order2['id'], order2['name'], order2['temp'],
                              order2['shelfLife'], order2['decayRate'])
            self.assertIsNone(new_order)
        except Exception as ex:
            self.assertIsInstance(ex, ValueError)

        # invliad decayRate
        order2 = { "id": "0ff534a7-a7c4-48ad-b6ec-7632e36af950",
                  "name": "Cheese Pizza",
                  "temp": "hot",
                  "shelfLife": 300,
                  "decayRate": 1.15}
        try:
            new_order = Order(order2['id'], order2['name'], order2['temp'],
                              order2['shelfLife'], order2['decayRate'])
            self.assertIsNone(new_order)
        except Exception as ex:
            self.assertIsInstance(ex, ValueError)
