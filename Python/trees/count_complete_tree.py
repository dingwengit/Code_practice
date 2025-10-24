# complete tree is a tree with both children exists or empty & equal count of left & right grand-children (don't
# check the values)
"""
           5
         /    \
        -4    -3
        / \
       8  20
output: 4 (nodes: 8, 20, -4, -3)

           15
         /    \
        11    23
        / \   /
       8  12 22
output: 4

"""
from tree import node

def count_complete_tree(root):
    cnt = 0

    def count_tree(r):
        nonlocal cnt
        if not r:
            return 0, True

        if not r.left and not r.right:
            cnt += 1
            return 1, True
        # if not r.left or not r.right:
        #     return 0, False
        l_c, l_is_comp = count_tree(r.left)
        r_c, r_is_comp = count_tree(r.right)
        # print(f"r.val={r.val}, l_c={l_c}, r_c={r_c}, l_is_comp={l_is_comp}, r_is_comp={r_is_comp}")
        if l_is_comp == False or r_is_comp == False or l_c != r_c:
            return 0, False
        cnt += 1
        return 1+l_c+r_c, True

    count_tree(root)
    return cnt

root = node(15)
root.left = node(11)
root.left.left = node(8)
root.left.right = node(12)
root.right = node(23)
root.right.left = node(22)
# root.right.right = node(25)

print(count_complete_tree(root))