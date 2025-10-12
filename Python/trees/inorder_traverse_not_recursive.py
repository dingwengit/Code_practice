"""
           5 (prev)
         /    \
(cur)   -4    -3
        / \   / \
(next) 8  20 2  11

Impletment in-order tranversal of a tree without recursive
Stack:
(5, False) -- (value, processed?)
(-3, False), (5, True), (-4, False), res: []
(-3, False), (5, True), (20, False), (-4, True), (8, False), res: []
(-3, False), (5, True), (20, False), (-4, True), res: [8] -- node 8 is a leaf node
(-3, False), (5, True), (20, False), res: [8, -4]
(-3, False), (5, True), res: [8, -4, 20]
(-3, False), res: [8, -4, 20, 5]
(11, False), (-3, True), (2, False) res: [8, -4, 20]
...
"""
import tree

def inorder_traverse_stack(root):
    res = []
    stack = [(root, False)]
    while(stack):
        print(stack)
        print(res)
        node, processed = stack.pop()
        if not node:
            continue
        if processed:
            res.append(node.val)
        elif not node.left and not node.right:
            res.append(node.val)
        else:
            stack.append((node.right, False))
            stack.append((node, True))
            stack.append((node.left, False))
    return res


root, n1, n2 = tree.node().get_one_tree_2_children()
print(inorder_traverse_stack(root))
