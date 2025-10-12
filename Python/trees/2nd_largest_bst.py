"""
           15
         /    \
        10    33
        / \   / \
       8  11 32  41
                 /
                35
Find the 2nd largest value in BST

Solution: in-order tranverse will return ascent order, then change "in-order traverse"
by right-child -> parent -> left-child, it will return descent order, it is better
"""

class tree:
    def __init__(self, v, lc=None, rc=None):
        self.lc, self.rc, self.v = lc, rc, v


visits, val = 0, None
def find_2nd_largest_node_method2(node):
    global visits, val
    if node and visits < 2:
        find_2nd_largest_node_method2(node.rc)
        visits += 1
        print(f"node={node.v}, visits={visits}")
        if visits == 2:
            val = node.v
            return
        find_2nd_largest_node_method2(node.lc)

r = tree(v=15)
r.lc = tree(v=10)
r.lc.lc = tree(v=8)
r.lc.rc = tree(v=11)

r.rc = tree(v=33)
r.rc.lc = tree(v=32)
r.rc.rc = tree(v=41)
r.rc.rc.lc = tree(v=35)
# print(find_2nd_largest_node(r))
find_2nd_largest_node_method2(r)
print(val)