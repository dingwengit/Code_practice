#!/usr/bin/env python

# Given price per length, write a function to return max sum of price for
# the rod (len = price.length)
# for example, the rod with length 8 below -- you can sell the rod with 4
# len 1, 2 len 2 = 14; or sell the rod as a whole of len 8 = 11
# len = array index + 1
# price_list = [(1, 1), (2, 4), (3, 4), (4, 6), (5, 7), (6, 9), (7, 12), (8, 11)]
# cur_max       (1, 1), (2, 4), (3, 5), (4, 8), (5, 9)
"""
1: (1/1)
2  (3/2)
3  (3/2)
4  (6/4)
5  (6/4)
6  (9/6)
7  (12/7)
8  (12/7)
19  (12/7)


len (1, 1) (2, 5)
1  1
2  5
3  6
4  10
5  5
6  6
7  7
8  8
"""

# input: len = 8
# output: 8 of len 1 for 1, or 4 of len 2 for 20, or 1 of len 8 for 11

def get_max_profit(l_p, l):
    max_profit = 0

    def rod_cutting(l_p, l, st=0, res=[]):
        nonlocal max_profit
        if l == 0:
            profit = sum([item[1] for item in res])
            # print(f"p={profit}, res={res}")
            max_profit = max(max_profit, profit)
            return
        for idx in range(st, len(l_p)):
            if l_p[idx][0] <= l:
                res.append(l_p[idx])
                rod_cutting(l_p, l - l_p[idx][0], idx, res)
                del res[-1]
    rod_cutting(l_p, l)
    return max_profit

l_p = [(1, 1), (2, 3), (3, 3), (4, 6), (5, 7), (6, 9), (7, 12), (8, 11)]
l = 10
print(get_max_profit(l_p, l))