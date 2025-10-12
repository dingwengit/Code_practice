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

def printTree(root):
    res = []  # 0 - root, 1 - left, 2 - right
    center = 40
    gap = 6

    def get_indent(n):
        return "".join([" "] * n)

    def print_tree(root):
        res.append((root, 0, center))
        prev_layer, layer, val_content, space_content, prev_indent = -1, 0, "", "", 0
        while (len(res) > 0):
            node, layer, indent = res.pop(0)
            if layer > prev_layer:
                val_content, space_content, prev_indent = "", "", 0
                prev_layer = layer

            # print(f"node={node.val}, layer={layer}, indent={indent}, prev_indent={prev_indent}")
            if node.left:
                res.append((node.left, layer+1, indent - 5))
            if node.right:
                res.append((node.right, layer+1, indent - 5 + gap))

            val_content += get_indent(indent - prev_indent + 2) + f"{node.val}"
            if node.left and node.right:
                space_content += get_indent(indent - prev_indent - 2 if space_content != "" else indent - 2) + "/" + get_indent(gap) + "\\"
            elif node.left:
                space_content += get_indent(indent - prev_indent - 2 if space_content != "" else indent - 2) + "/"
            elif node.right:
                space_content +=get_indent(indent - prev_indent - 2 if space_content != "" else indent - 2) + get_indent(gap) + "\\"

            if len(res) == 0 or res[0][1] > layer:
                print(val_content)
                print(space_content)
            prev_indent = indent

    print_tree(root)

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
"""
new_root
           15                
         /    \
        11    23
        / \   / \
       8  12 22  25
"""
'''
     2, 3, 4, 5, 6
prefix   = [1, 1*2, 1*2*3, 1*2*3*4, 1*2*3*4*5]
suffix   = [1*6*5*4*3, 1*6*5*4, 1*6*5, 1*6, 1]

([abc)[aaa]
stack
'''
#
# root = node(15)
# root.left = node(11)
# root.left.left = node(8)
# root.left.right = node(12)
# root.right = node(23)
# root.right.left = node(22)
# root.right.right = node(25)
#
# printTree(root)

#
# traverse(root)

def reverse_tree(root):
    if not root:
        return
    traverse(root.left)
    traverse(root.right)

    root.right, root.left = root.left, root.right