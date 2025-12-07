# Given an infinite number of quarters (25 cents), dimes (10 cents), nickels
# (5 cents) and pennies (1 cent),
# write code to calculate the number of ways of representing n cents.
# Noted problem : in this method, n=10, "1,1,1,1,1,5" will be different than
# "5,1,1,1,1,1", and "1,5,1,1,1,1", ....

def get_coin_changes(coins, total, st=0, res=[]):
    if total == 0:
        print(res)
        return

    for idx in range(st, len(coins)):
        if coins[idx] <= total:
            res.append(coins[idx])
            get_coin_changes(coins, total - coins[idx], idx, res)
            del res[-1]

coins = [25, 10, 5, 1]
n = 40
get_coin_changes(coins, n)