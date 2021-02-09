#!/usr/bin/env python

# Given price per length, write a function to return max sum of price for
# the rod (len = price.length)
# for example, the rod with length 8 below -- you can sell the rod with 4
# len 1, 2 len 2 = 14; or sell the rod as a whole of len 8 = 11
# len = array index + 1

max_price = 0

def find_max_price(price, idx, lengh, res):
    if lengh == 0:
        print("max price {} from {}".format(sum(res), res))
        return

    for i in range(len(price)):
        l = i + 1
        if l <= lengh and i >= idx:
            res.append(price[i])
            find_max_price(price, i, lengh - l, res)
            del res[len(res) - 1]


def find_max_price2(price, idx, length, res):
    global max_price
    if length == 0:
        max_price = max(max_price, sum(res))
        print("max price2 {} from {}".format(sum(res), res))
        return

    for i in range(idx, len(price)):
        if i + 1 <= length:
            res.append(price[i])
            find_max_price2(price, i, length - i - 1, res)
            del res[len(res) - 1]
        else:
            break

price_list = [1, 5, 4, 6, 7, 9, 12, 11]
find_max_price(price_list, 0, 8, [])
find_max_price2(price_list, 0, 8, [])
print(max_price)
