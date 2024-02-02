# finding all possible order of arrangements of a given set of letters
# print(permute(1, ["a","b","c"])) --> ['a', 'b', 'c']
# print(permute(2, ["a","b","c"])) --> ['aa', 'ab', 'ac', 'ba', 'bb', 'bc',
# 'ca', 'cb', 'cc']

def permute2(n, s, res, idx=0):
    for i in range(0, len(s)):
        res[idx] = s[i]
        if idx >= n-1:
            print(''.join(res[:idx+1]))
        else:
            permute2(n, s, res, idx+1)


def permute(len, s):
    if len == 1:
        return s
    else:
        return [ x + y
                 for x in s
                 for y in permute(len-1, s)]


# print(permute(1, ['a', 'b', 'c']))
# print(permute(2, ['a', 'b', 'c']))

s="abc"
res = [''] * len(s)
permute2(3, s, res)
