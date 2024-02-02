#!/usr/bin/env python

# Given price per length, write a function to return max sum of price for
# the rod (len = price.length)
# for example, the rod with length 8 below -- you can sell the rod with 4
# len 1, 2 len 2 = 14; or sell the rod as a whole of len 8 = 11
# len = array index + 1
# price_list = [1, 5, 4, 6, 7, 9, 12, 11]
# input: len = 8
# output: 8 of len 1 for $1, or 4 of len 2 for $20, or 1 of len 8 for $11

max_price = 0


def find_max_price3(p, l, idx=0, cur_len=0, res=[]):
    global max_price
    if cur_len == l:
        print("max price {} from {}".format(sum(res), res))
        max_price = max(max_price, sum(res))
        return
    if idx + 1 <= l and cur_len + idx + 1 <= l:
        # take idx
        res.append(p[idx])
        cur_len += (idx + 1)
        find_max_price3(p, l, idx, cur_len, res)
        # skip idx, and take idx + 1
        del res[len(res)-1]
        cur_len -= (idx + 1)
        find_max_price3(p, l, idx+1, cur_len, res)


def find_max_price(price, idx, lengh, res):
    global max_price
    if lengh == 0:
        print("max price {} from {}".format(sum(res), res))
        max_price = max(max_price, sum(res))
        return

    for i in range(idx, len(price)):
        if i+1 <= lengh:
            res.append(price[i])
            find_max_price(price, i, lengh - (i+1), res)
            del res[len(res) - 1]


price_list = [1, 5, 4, 6, 7, 9, 12, 11]
find_max_price(price_list, 0, 8, [])
print(max_price)
max_price = 0
find_max_price3(price_list, 8)
print(max_price)
