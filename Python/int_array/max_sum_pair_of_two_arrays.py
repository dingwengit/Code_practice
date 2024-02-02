#!/usr/bin/env python
from array import *

# given two arrays of N length, find out the max sum of selecting elements
# from the two arrays -- how many elements?
# ** with no same index and no continous positions in the same array **
# a = [2, 3, 9, 11]
# b = [5, 1, 8, 2]
# max sum = 5 + 8 + 3 + 11
# need more clarifications on this

def max_sum_pair(a, b):
    c1 = [0] * len(a)
    c2 = [0] * len(b)

    for i in range(len(a)): # a, b has the same length
        if i == 0:
            c1[i] = a[i]
            c2[i] = b[i]
            continue
        # current max i = max of prev_max1 and prev_max2 + a[i]
        c1[i] = max(c1[i-1], max(0, c2[i-1]) + a[i])
        if i >= 2: # this way, we can skip another array's element
            c1[i] = max(c1[i], c1[i-2] + a[i])
        c2[i] = max(c2[i-1], max(0, c1[i-1]) + b[i])
        if i >= 2: # this way, we can skip another array's element
            c2[i] = max(c2[i], c2[i-2] + b[i])

    return max(c1[len(a)-1], c2[len(a)-1])

if __name__ == '__main__':
    a = [2, 3, 9, 11]
    b = [5, 1, 8, 2]
    print(max_sum_pair(a, b))