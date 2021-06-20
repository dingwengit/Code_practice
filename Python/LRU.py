import threading

class DoubleLinkList:
    def __init__(self, key, pv=None, nt=None, value=None):
        self.key = key
        self.pv = pv
        self.nt = nt
        self.data = value


class LRU:
    def __init__(self, size):
        self.total_size = size
        self.size = 0
        self.head = DoubleLinkList()
        self.tail = DoubleLinkList()
        self.hash = dict()
        self.lock = threading.Lock()

    def remove_head(self):
        del self.hash[self.head.key]
        self.head.nt.pv = None
        tmp = self.head.nt
        self.head.nt = None
        self.head = tmp

    def read(self, key):
        # use key to find index in list
        # if index is not the latest, move to the end of list
        with self.lock:
            node = hash[key]
            if node == self.tail:
                return node.data
            # delete node from LL
            if self.head == node:
                self.remove_head()
            else:
                node.pv.nt = node.nt
            node.nt.pv = node.pv
            # append node to the tail
            self.tail.nt = node
            node.pv = self.tail
            node.nt = None
            self.tail = node

    def add(self, key, value):
        with self.lock:
            # add k,v into ll
            if self.size >= self.total_size:
                self.remove_head()
                self.size -= 1
            # add to the tail -- <- tail -> node
            node = DoubleLinkList(key=key, pv = self.tail, value=value)
            self.hash[key] = node
            self.tail.nt = node
            self.tail = node
            self.size += 1
