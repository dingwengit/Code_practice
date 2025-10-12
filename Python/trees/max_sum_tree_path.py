# given binary tree, write a function to return max path sum
# path is a collection of connected nodes. No node will connect to more than
# 2 other nodes
"""
           5
         /    \
        -4    -3
        / \   / \
       8  20 2  11
"""
import sys
from tree import node

path_max = -1 * sys.maxint


def find_max_path_sum(n):
    global path_max
    if not n:
        return 0

    l_sum = find_max_path_sum(n.left)
    r_sum = find_max_path_sum(n.right)
    #l_sum or r_sum could be negative
    l_max = max(l_sum + n.val, n.val) # max left side path
    r_max = max(r_sum + n.val, n.val) # max right side path
    path_max = max(path_max, max(n.val, n.val + l_sum + r_sum), max(n.val+l_max, l_max), max(n.val + r_max, r_max))

    return max(l_max, r_max)


root = node().get_one_tree()
find_max_path_sum(root)
print(path_max)

