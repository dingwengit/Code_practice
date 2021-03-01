from tree import node


# problem of this method is to return one of the nodes if they are parent-child
# relationship
def LCA(root, n1, n2):
    if root is None:
        return None

    if root == n1 or root == n2:
        return root

    l = LCA(root.left, n1, n2)
    r = LCA(root.right, n1, n2)

    if l and r:
        return root

    return l if l else r

# better solution
def find_lca(root, n1, n2):
    if root is None:
        return 0, None
    l_found, parent = find_lca(root.left, n1, n2)
    if l_found == 2:
        return l_found, root
    r_found, parent = find_lca(root.right, n1, n2)
    if r_found == 2:
        return r_found, root
    n_found = l_found + r_found + (n1, n2).count(root)
    return n_found, root if n_found == 2 else None

root, n1, n2 = node().get_one_tree_2_children()
lca = LCA(root, n1, n2)
print(lca.val)
n_found, node = find_lca(root, n1, n2)
print("n_found: {}, lca: {}".format(n_found, node.val))