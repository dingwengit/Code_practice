# Given a binary tree with an integer of each node, and an integer X
# find if there is a tree path exists where sum of the path equals to X

'''
           5   --> node (5), input: lc_path=(-4,4,16), c_val=5, rc_path=(-3,-1,8) -> find all combinations with 2 loops
         /    \
        -4    -3  --> node (-4), input: lc_path=[8], rc_path = [20], return set (-4, -4+8, -4+20)
        / \   / \  --> node (-3), input: lc_path=[2], rc_path = [11], return set (-3, -3+2, -3+11)
       8  20 2  11


'''