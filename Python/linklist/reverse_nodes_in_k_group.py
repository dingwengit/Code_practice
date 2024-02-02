'''
given a linked list, reverse the nodes of sub link list of len k at a time

input: 1->2->3->4->5->6->7
k = 3
nodes = [1, 2, 3]
     -   1->2->3   4
    pn, fn,   ln, nn

output: 3->2->1->6->5->4->7

edge cases:
k = 1
ll: 1->2
'''

class linkList:
    def __init__(self, v, next=None):
        self.v, self.next = v, next


def reverse_k_node(head, k):
    if k <= 1:
        return head
    pn, new_head, nn, nodes = None, head, None, []
    while (head):
        nodes.append(head)
        nn = head.next
        if len(nodes) == k:
            nodes[0].next = nn
            while(len(nodes)>0):
                fn = nodes.pop()
                if not pn:
                    new_head = fn
                if pn:
                    pn.next = fn
                pn = fn
                print(f"pn:{pn.v}, new_head:{new_head.v}, fn:{fn.v}")
        head = nn

    return new_head


head = linkList(1)
head.next = linkList(2)
head.next.next = linkList(3)
head.next.next.next = linkList(4)
head.next.next.next.next = linkList(5)
head.next.next.next.next.next = linkList(6)
head.next.next.next.next.next.next = linkList(7)
head.next.next.next.next.next.next.next = linkList(8)

new_head = reverse_k_node(head, 4)
while(new_head):
    print(new_head.v)
    new_head = new_head.next
