# give string "abc", print out its combinations
# result: "a", "b", "c", "ab", "bc", "ac"

def str_combinations(s, st, k, res):
    for i in range(st, len(s)):
        res[k] = s[i]
        print ''.join(res[:k+1])
        str_combinations(s, i+1, k+1, res)

s = "abc"
res = [''] * len(s)
str_combinations(s, 0, 0, res)
