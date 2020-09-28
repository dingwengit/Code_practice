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

path_max = -1 * sys.maxint


class node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def find_max_path_sum(n):
    global path_max
    if not n:
        return 0

    l_sum = find_max_path_sum(n.left)
    r_sum = find_max_path_sum(n.right)

    if n.val + l_sum + r_sum > path_max:
        path_max = n.val + l_sum + r_sum

    return max(max(l_sum + n.val, n.val), max(r_sum + n.val, n.val))


root = node(5)
root.left = node(-4)
root.left.left = node(8)
root.left.right = node(20)
root.right = node(-3)
root.right.left = node(2)
root.right.right = node(11)
find_max_path_sum(root)
print path_max

