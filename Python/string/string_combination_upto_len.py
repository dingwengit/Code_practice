# give string "abc", print out its combinations
# result: "a", "b", "c", "ab", "bc", "ac"

def str_combinations(s, st, k, res):
    for i in range(st, len(s)):
        res[k] = s[i]
        print(''.join(res[:k+1]))
        str_combinations(s, i+1, k+1, res)


def str_combinations_upto_len(s, st, idx, res, length):
    for i in range(st, len(s)):
        res[idx] = s[i]
        if idx + 1 == length:
            print(''.join(res[:idx+1]))
        if idx + 1 < length:
            str_combinations_upto_len(s, i+1, idx+1, res, length)

# abcd
# len:3           a (i=0)
# len:2    bcd
#         b (j=1)                        c (j=1)
# len:1   c, d  --> ['abc', 'abd']     d --> ['acd']
#
# len:3           b (i=1)
# len:2    cd
#         c (j=1)
# len:1  d --> ['bcd']


def combination_with_len(n, s):
    if n == 1:
        return s
    else:
        return [ x + y
                 for i, x in enumerate(s[:len(s)-n+1])
                 for y in combination_with_len(n-1, s[i+1:])]


s = "abc"
res = [''] * len(s)
str_combinations(s, 0, 0, res)
s = "abcde"
n = 4
print("results for len={}".format(n))
res = [''] * len(s)
str_combinations_upto_len(s, 0, 0, res, n)
print("combination results for len={}".format(n))
print(combination_with_len(n, s))
