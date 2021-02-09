# Given an infinite number of quarters (25 cents), dimes (10 cents), nickels
# (5 cents) and pennies (1 cent),
# write code to calculate the number of ways of representing n cents.
# Noted problem : in this method, n=10, "1,1,1,1,1,5" will be different than
# "5,1,1,1,1,1", and "1,5,1,1,1,1", ....


def coin_change(a, idx, n, res):
    if n == 0:
        print res
        return

    for i in range(len(a)):
        if i >= idx and a[i] <= n:
            res.append(a[i])
            coin_change(coins, i, n - a[i], res)
            del res[len(res) - 1]


coins = [25, 10, 5, 1]
n = 40
res = []
coin_change(coins, 0, n, res)
