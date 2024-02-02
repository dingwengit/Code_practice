  # given an integer, generate all binary trees
# e.g., n=3,
# output:
# 0          0              0          0        0
#  \          \            / \        /        /
#   0          0          0   0      0        0
#    \        /                       \      /
#     0      0                         0    0
from tree import node

def get_binary_trees(num):
    if num == 0:
        return [None]
    cur_res = []
    for left_n in range(num):
        right_n = num - 1 - left_n
        left_trees = get_binary_trees(left_n)
        right_trees = get_binary_trees(right_n)
        cur_res += [node(data=left_n, left=left, right=right) for left in left_trees
                    for right in right_trees]
    return cur_res

# given a sorted array a=[1,3,5,7,9], print out all possible BSTs
def get_bst(a):
    if len(a) <= 0:
        return [None]
    res = []
    for idx in range(len(a)):
        left_trees = get_bst(a[:idx])
        right_trees = get_bst(a[idx+1:])
        res += [node(data=a[idx], left=lt, right=rt) for lt in left_trees
                for rt in right_trees]
    return res


print(get_binary_trees(3))
a = [1,3,5]
print(get_bst(a))