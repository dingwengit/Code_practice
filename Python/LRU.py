import threading


class DoubleLinkList:
    def __init__(self, key, pv=None, nt=None, value=None):
        self.key, self.pv, self.nt, self.data = key, pv, nt, value

#
# h <-> n1 <-> n2 <-> n3 <-> n4 <-> t <-> n
#
class LRU:
    def __init__(self, size):
        self.total_size = size
        self.size = 0
        self.head = DoubleLinkList()
        self.tail = DoubleLinkList()
        self.hash = dict()
        self.lock = threading.Lock()

    def read(self, key):
        # use key to find index in list
        # if index is not the latest, move to the end of list
        with self.lock:
            node = hash[key]
            if node == self.tail:
                return node.data
            if node == self.head:
                self.head = node.nt
            # remove node from ll
            node.nt.pv = node.pv
            node.pv.nt = node.nt
            # append node to the tail
            node.pv = self.tail
            self.tail.nt = node
            node.nt = None
            self.tail = node
            return node.data

    def add(self, key, value):
        with self.lock:
            # add k,v into ll
            if self.size >= self.total_size:
                del self.hash[self.head.key]
                self.head.nt.pv = None
                self.head = self.head.nt
                self.size -= 1
            # add to the tail -- <- tail -> node
            node = DoubleLinkList(key=key, value=value)
            self.hash[key] = node
            node.pv = self.tail
            node.nt = None
            self.tail.nt = node
            self.tail = node
            self.size += 1
