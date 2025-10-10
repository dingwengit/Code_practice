# Given a binary tree with an integer of each node, and an integer X
# find if there is a tree path exists where sum of the path equals to X

'''
tree1
           15
         /    \
        10    33
        / \   / \
       8  11 32  41
                 /
                35

tree2           
           5   --> node (5), input: l_path=(-4,4,16), c_val=5, r_path=(-3,-1,8) -> find all combinations with 2 loops
         /    \
        -4    -3  --> node (-4), input: l_path=[8], r_path = [20], return set (-4, -4+8, -4+20)
        / \   / \  --> node (-3), input: l_path=[2], r_path = [11], return set (-3, -3+2, -3+11)
       8  20 2  11
'''

class tree:
    def __init__(self, v, l=None, r=None):
        self.l, self.r, self.v = l, r, v

found = False
def find_number(node, x):
    global found
    if found or node is None:
        return []
    l_sums = find_number(node.l, x)
    r_sums = find_number(node.r, x)
    if node.v == x:
        found = True
    if found:
        return []
    res = [node.v]
    for l_sum in l_sums:
        res.append(node.v + l_sum)
        if node.v + l_sum == x:
            found = True
            return []
        for r_sum in r_sums:
            res.append(node.v + r_sum)
            if node.v + r_sum == x or node.v + l_sum + r_sum == x:
                found = True
                return []
    return res

r = tree(v=15)
r.l = tree(v=10)
r.l.l = tree(v=8)
r.l.r = tree(v=11)

r.r = tree(v=33)
r.r.l = tree(v=32)
r.r.r = tree(v=41)
r.r.r.l = tree(v=35)
find_number(r, 98)
print(f"found={found}")