
#
# method1 is to use hashtable
# time and space complexity is both O(h), h is the height of the tree
#
import tree

def find_lca_1(root, n1, n2):
    if root == n1 or root == n2:
        return root

    nodes = set()
    n = n1
    while(n):
        n = n.parent
        nodes.add(n)

    n = n2
    while(n and n not in nodes):
        n = n.parent
    return n

# find the deeper node and move the same level as the other node
# then move up together
def find_lca_2(root, n1, n2):
    def get_depth(node):
        depth = 0
        while node:
            depth += 1
            node = node.parent
        return depth

    d1, d2 = map(get_depth, (n1, n2))
    n = n1 if d1 > d2 else n2
    d_diff = abs(d2 - d1)
    while d_diff:
        n = n.parent
        d_diff -= 1

    if d1 > d2:
        n1 = n
    else:
        n2 = n
    while n1 != n2:
        n1, n2 = n1.parent, n2.parent

    return n1


root, n1, n2 = tree.node().get_one_tree_with_parent()
node = find_lca_1(root, n1, n2)
print(node.val)
root, n1, n2 = tree.node().get_one_tree_with_parent()
node = find_lca_2(root, n1, n2)
print(node.val)