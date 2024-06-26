#!/usr/bin/env python

'''
In share trading, a buyer buys shares and sells on a future date. Given the stock price of n days, the trader is allowed to make at most k transactions, where a new transaction can only start after the previous transaction is complete, find out the maximum profit that a share trader could have made.
Examples:

         10, 22, 5, 75, 65, 80
p[*][1]  0   12  12 70  70  75
p[*][2]  0   12  12 82  82  87
trades = [(10, 22)]

Input:
Price = [10, 22, 5, 75, 65, 80]
    K = 2
Output:  87
Trader earns 87 as sum of 12 and 75
Buy at price 10, sell at 22, buy at
5 and sell at 80

Input:
Price = [100, 30, 15, 10, 8, 25, 80]
    K = 3
Output:  72
Only one transaction. Buy at price 8
and sell at 80.

Input:
Price = [90, 80, 70, 60, 50]
    K = 1
Output:  0
Not possible to earn.

'''

# option 1 -- backtrack
# time complexity O(k * N^2), space: O(K)
def find_max_profit(a, idx, k, res):
    global max_p
    if k <= len(res):
        return

    for i in range(idx + 1, len(a)):
        cur_p = a[i] - a[idx]
        if cur_p > 0:
            res.append((a[i], a[idx], cur_p))
            max_p = max(max_p, sum(p for _,_,p in res))
            find_max_profit(a, i+1, k, res)
            del res[len(res)-1]

def print_max_profit(a, k):
    res = []
    find_max_profit(a, 0, k, res)
    print(max_p)

# option 2 -- dynamic programming
# p[i][j] -- max profit when buy / sell stock to day [i] with j trades
# time complexity O(K * N^2), space: O(K * N)
def get_max_profit(a, k):
    n = len(a)
    p = [[0 for i in range(k + 1)] for _ in range(n)]

    for i in range(1, n):
        for j in range(1, k+1):
            max_p = 0
            for m in range(i):
                if a[i] - a[m] > 0:
                    max_p = max(max_p, a[i] - a[m] + p[m][j-1])
            p[i][j] = max(max_p, p[i-1][j])

    return p[n-1][k]


# option 3 -- based on option 2
# p[i][t] -- max profit when buy / sell stock to day [i] with t trades
# max_p = max(p[i-1][t], max(a[i] - a[m] + p[m][t-1])) for m in [1, i-1]
# then max(a[i] - a[m] + p[m][t-1]) = a[i] + max(p[m][t-1]- a[m]) for m in [1, i-1]
# = a[i] + max(p[m][t-1]- a[m], p[i-1][t-1] - a[i-1]) for m in [1, i-2]
# time complexity O(K * N), space: O(K * N)
def get_max_profit_linear(a, k):
    n = len(a)
    p = [[ 0 for i in range(k+1)] for _ in range(n)]

    for t in range(1,k+1):
        prev_diff = float('-inf')
        for i in range(1, n):
            prev_diff = max(prev_diff, p[i-1][t-1] - a[i-1])
            p[i][t] = max(p[i-1][t], a[i] + prev_diff)
    return p[n-1][k]


max_p = 0
a = [90, 80, 70, 60, 50]
k = 1
print(get_max_profit_linear(a, k))
# print_max_profit(a, k)
max_p = 0
a = [10, 22, 5, 75, 65, 80]
k = 2
# print(get_max_profit_linear(a, k))
print_max_profit(a, k)
max_p = 0
a = [100, 30, 15, 10, 8, 25, 80]
k = 3
print(get_max_profit_linear(a, k))
# print_max_profit(a, k)
