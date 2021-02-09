"""
both structual and values are the same in the sub-trees
(1) not symmetric, because values are different
            5
         /    \
        -4    -3
        / \   / \
       8  20 2  11
(1) not symmetric, because structure are different
            5
         /    \
        -4    -3
        / \   / \
       8  20 2
(3) symmetric
            5
         /    \
        -4    -4
        / \   / \
       8  20 20  8
      /           \
    10            10
"""
import tree


def check_symmetric_tree(node):
    def check_symmetric_subtrees(l_n, r_n):
        if not l_n and not r_n:
            return True
        elif l_n and r_n:
            if l_n.val == r_n.val:
                return check_symmetric_subtrees(l_n.left, r_n.right) and \
                       check_symmetric_subtrees(l_n.right, r_n.left)
        return False

    return not node or check_symmetric_subtrees(node.left, node.right)

root = tree.node().get_symmetric_tree()
print(check_symmetric_tree(root))