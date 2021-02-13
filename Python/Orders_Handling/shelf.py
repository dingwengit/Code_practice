from threading import Lock
import random
from order import ORDER_PICKEDUP, ORDER_WASTED

CAPACITY = 10
OVERFLOW_CAPACITY = 15
OVERFLOW_SHELF_NAME = "overflow"


class Shelf():
    def __init__(self, temperature, overflow=False):
        self.temperature = temperature
        self.is_overflow = overflow
        self.capacity = OVERFLOW_CAPACITY if overflow else CAPACITY
        self.orders = dict()
        self.lock = Lock()

    def __repr__(self):
        ret = ["\r\n"]
        idx = 1
        for order in self.orders.values():
            ret += "{} - {}\r\n".format(idx, order)
            idx += 1
        return ''.join(ret)

    def add_order(self, order):
        with self.lock:
            assert order.id not in self.orders, \
                "order id {} already exists on shelf {}"\
                    .format(order.id, self.temperature)
            assert order.temperature == self.temperature or \
                   self.is_overflow, \
                "order temp {} is different than shelf's temperature {}"\
                    .format(order.temperature, self.temperature)
            if len(self.orders) >= self.capacity:
                print("Shelf {} is at its capacity, cannot add "
                      "order {}".format(self.temperature, order))
                return False
            self.orders[order.id] = order
            return True

    def pickup_order(self, order_id, moved=False):
        with self.lock:
            if order_id in self.orders:
                order = self.orders[order_id]
                del self.orders[order_id]
                if moved:
                    print("< moved out order {} from shelf {}"\
                        .format(order, self.temperature))
                else:
                    order.order_state = ORDER_PICKEDUP
                    # we need check value again
                    if order.get_value() == 0:
                        order.order_state = ORDER_WASTED
                    print("< picked up order {} from shelf {}" \
                          .format(order, self.temperature))
                return order
            return None

    def has_capacity(self):
        with self.lock:
            return len(self.orders) < self.capacity

    def dispose_random_order(self):
        with self.lock:
            order_id = random.sample(self.orders.keys(), k=1)[0]
            order = self.orders[order_id]
            del self.orders[order_id]
            print("< disposed {} order {} as waste"
                  .format(self.temperature, order))
            return order

    def cleanup_orders(self):
        """
        The purpose of this method is to remove 2 kinds of orders
        (1) orders with 0 value, (2) orphan orders with picked_up = True
        :return:
        """
        removed = False
        with self.lock:
            remove_orders = [order for order in self.orders.values() if
                             order.get_value() == 0 or
                             order.order_state == ORDER_PICKEDUP or
                             order.order_state == ORDER_WASTED]
            for item in remove_orders:
                print("< cleanup thread removed order {} from shelf {}"
                      .format(item, self.temperature))
                del self.orders[item.id]
                if item.get_value() == 0:
                    item.order_state = ORDER_WASTED
                removed = True
        return removed

