"""
           5
         /    \
        -4    -3
        / \   / \
       8  20 2  11

find successor for a given Node, in BST tree or in-order tranverse path

"""
import tree

def find_successor(node):
    # case 1: if node has right child, the successor would the right tree's
    # most left node
    if node.right:
        while node.right:
            node = node.right
            while node.left:
                node = node.left
        return node

    # case 2: node's sucessor is on parent path, while the parent's right
    # child is node
    while node.parent and node.parent.right == node:
        node = node.parent
    # if node goes to root, then it is the leaf node in the right tree,
    # no successor
    return node.parent

root, n1, n2 = tree.node().get_one_tree_with_parent()
suc = find_successor(n2)
print( suc.val )