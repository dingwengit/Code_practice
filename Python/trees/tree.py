"""
           5
         /    \
        -4    -3
        / \   / \
       8  20 2  11
"""

class node:
    def __init__(self, data=None, parent=None, left=None, right=None):
        self.parent, self.left, self.right, self.val = parent, left, right, \
                                                       data

    def __repr__(self):
        res = []
        def print_tree(root, tag):
            if root:
                res.append("{}-{} ".format(tag, root.val))
                print_tree(root.left, "{}-l".format(root.val))
                print_tree(root.right, "{}-r".format(root.val))
        print_tree(self, "r")
        return ''.join(res)

    def get_one_tree_with_parent(self):
        root = node(data=5)
        root.left = node(data=-4, parent=root)
        root.left.left = node(data=8, parent=root.left)
        root.left.right = node(data=20, parent=root.left)
        root.right = node(data=-3, parent=root)
        root.right.left = node(data=2, parent=root.right)
        root.right.right = node(data=11, parent=root.right)
        return root, root.left.right, root.right.left

    def get_one_tree(self):
        root = node(1)
        root.left = node(0)
        root.left.left = node(1)
        root.left.right = node(0)
        root.right = node(0)
        root.right.left = node(1)
        root.right.right = node(0)
        return root

    def get_one_tree_2_children(self):
        root = node(5)
        root.left = node(-4)
        root.left.left = node(8)
        root.left.right = node(20)
        root.right = node(-3)
        root.right.left = node(2)
        root.right.right = node(11)
        return root, root.right.left, root.right.right


    def get_symmetric_tree(self):
        root = node(5)
        root.left = node(-4)
        root.left.left = node(8)
        root.left.right = node(21)
        root.right = node(-4)
        root.right.left = node(21)
        root.right.right = node(8)
        root.right.right.right = node(30)
        root.left.left.left = node(30)
        return root


def traverse(root):
    if not root:
        return
    traverse(root.left)
    print(root.val)
    traverse(root.right)

"""
           15
         /    \
        11    23
        / \   / \
       8  12 22  25
"""
# root = node(15)
# root.left = node(11)
# root.left.left = node(8)
# root.left.right = node(12)
# root.right = node(23)
# root.right.left = node(22)
# root.right.right = node(25)
#
# traverse(root)
