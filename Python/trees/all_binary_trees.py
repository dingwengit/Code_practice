  # given an integer presenting # of nodes, generate all binary trees
# e.g., n=3,
# output:
# 1          1              1          1        1
#  \          \            / \        /        /
#   2          2          2   3      2        2
#    \        /                       \      /
#     3      3                         3    3
from tree import node, printTree

def get_binary_trees(l, r):
    if l >= r:
        return [None]
    cur_res = []
    for idx in range(l, r):
        left_trees = get_binary_trees(l, idx)
        right_trees = get_binary_trees(idx+1, r)
        cur_res += [node(data=idx, left=left, right=right) for left in left_trees
                    for right in right_trees]
    return cur_res

# given a sorted array a=[1,3,5,7,9], print out all possible BSTs
def get_bst(a):
    if len(a) == 0:
        return [None]
    res = []
    for idx in range(len(a)):
        left_trees = get_bst(a[:idx])
        right_trees = get_bst(a[idx+1:])
        res += [node(data=a[idx], left=left, right=right) for left in left_trees
                for right in right_trees]
    return res

res = get_binary_trees(0, 4)

# a = [1,3,5]
# res = get_bst(a)

for t in res:
    printTree(t)
