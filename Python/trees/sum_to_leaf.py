"""
           5
         /    \
        -4    -3
        / \   / \
       8  20 2  11

Given a binary tree and integer K, find out if any sum of node values from
root-to-leaf path can be K
"""
import tree

def find_root_leaf_sum(root, remain_path_sum):
    if not root:
        return False
    if not root.left and not root.right:
        if root.val == remain_path_sum:
            return True
    else:
        return find_root_leaf_sum(root.left, remain_path_sum - root.val) or \
               find_root_leaf_sum(root.right, remain_path_sum - root.val)
    return False


root, n1, n2 = tree.node().get_one_tree_2_children()
print(find_root_leaf_sum(root, 22))