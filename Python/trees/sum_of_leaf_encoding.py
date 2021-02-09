"""
             1
          /    \
         0     0
        / \   / \
       1  0  1  1
root to leaf represent a binary format of integer (101) + (100) + (101) + (101)
                    = 5 + 4 + 5 + 5
"""
import tree

def get_sum_encoding_tree(root, path_sum=0):
    if root is None:
        return 0
    path_sum = path_sum * 2 + root.val
    if not root.left and not root.right:
        return path_sum
    return get_sum_encoding_tree(root.left, path_sum) + \
           get_sum_encoding_tree(root.right, path_sum)

root = tree.node().get_one_tree()
print(get_sum_encoding_tree(root))