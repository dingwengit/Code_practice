"""
           15
         /    \
        10    33
        / \   / \
       8  11 32  41
                 /
                35
Find the 2nd largest value in BST

case 1: root --> right_child ? yes --> move to right child
                               no --> left child? yes --> left tree's most right node
                                                  no --> no left child and no right child
"""

class tree:
    def __init__(self, v, lc=None, rc=None):
        self.lc, self.rc, self.v = lc, rc, v


def find_most_right_node(node):
    cur = node
    while(cur):
        if cur.rc:
            cur = cur.rc
        else:
            break
    return cur


def find_2nd_largest_node(root):
    prev, cur = None, root

    while(cur):
        if cur.rc:
            prev, cur = cur, cur.rc
            continue
        if cur.lc:
            prev = find_most_right_node(cur.lc)
        break
    return prev.v


r = tree(v=15)
r.lc = tree(v=10)
r.lc.lc = tree(v=8)
r.lc.rc = tree(v=11)

r.rc = tree(v=33)
r.rc.lc = tree(v=32)
# r.rc.rc = tree(v=41)
# r.rc.rc.lc = tree(v=35)
print(find_2nd_largest_node(r))
