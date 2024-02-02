# universal tree is a tree with equal count of left & right children (don't
# check the values)
"""
           5
         /    \
        -4    -3
        / \   / \
       8  20 2  11
output: 7
"""

from tree import node


def get_universal_trees(root):
    if root is None:
        return 0, True

    l_cnt, l_check = get_universal_trees(root.left)
    r_cnt, r_check = get_universal_trees(root.right)

    if l_check and r_check and l_cnt == r_cnt:
        return 1 + l_cnt + r_cnt, True
    else:
        return l_cnt + r_cnt, False


root = node().get_one_tree()
print(get_universal_trees(root))
