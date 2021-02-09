"""
           5 (prev)
         /    \
(cur)   -4    -3
        / \   / \
(next) 8  20 2  11

Impletement in-order tranverse of a tree without recursive
Stack:
(5, False)
(-3, False), (5, True), (-4, False), res: []
(-3, False), (5, True), (20, False), (-4, True), res: []
(-3, False), (5, True), (20, False), (-4, True), res: [8]
"""
import tree

def inorder_traverse_stack(root):
    res = []
    stack = [(root, False)]
    while(stack):
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


def inorder_traverse_linear(root):
    prev, cur = None, root
    res = []
    while(cur):
        if cur.parent == prev:
            if cur.left:
                next = cur.left
            else:
                res.append(cur.val)
                next = cur.right or cur.parent
        elif prev == cur.left: # left tree is done
            res.append(cur.val)
            next = cur.right or cur.parent
        else: # right tree is done
            next = cur.parent
        prev, cur = cur, next

    return res


root, n1, n2 = tree.node().get_one_tree_2_children()
print(inorder_traverse_stack(root))

root, n1, n2 = tree.node().get_one_tree_with_parent()
print(inorder_traverse_linear(root))