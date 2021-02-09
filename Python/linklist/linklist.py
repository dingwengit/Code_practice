
class linklist():
    def __init__(self, val):
        self.val, self.next = val, None

    def __repr__(self):
        def print_list(head):
            node = head
            res = []
            while(node):
                res.append(str(node.val))
                node = node.next
                if node:
                    res.append("->")
            return (''.join(res))
        return print_list(self)


def create_new_ll():
    head = linklist(1)
    head.next = linklist(2)
    head.next.next = linklist(3)
    return head


def reverse_ll(head):
    if not head:
        return head
    prev, cur, next = None, head, head.next
    while(cur):
        cur.next = prev
        prev = cur
        cur = next
        if cur:
            next = cur.next
    return prev


def reverse_ll_recursive(head):
    if head is None or head.next is None:
        return head

    new_head = reverse_ll_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head


head = create_new_ll()
print(head)
head=reverse_ll(head)
print(head)
print(reverse_ll_recursive(head))
