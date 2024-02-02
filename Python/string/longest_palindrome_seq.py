#problem : for input "character", the longest palindrome subsequence is "carac"

def find_LPS3(s, i, j):
    if len(s) == 0:
        return 0

    if i >= j:
        return 1

    if j - 1 == i and s[i] == s[j]:
        return 2

    if s[i] == s[j]:
        return 2 + find_LPS3(s, i+1, j-1)
    return max(find_LPS3(s, i+1,j), find_LPS3(s, i, j-1))


# recursive call
def find_LPS(s, i, j):
    if i == j:
        return 1, [s[i]]

    if i + 1 == j and s[i] == s[j]:
        return 2, [s[i], s[j]]

    if s[i] == s[j]:
        c, res = find_LPS(s, i+1, j-1)
        return c + 2, [s[i]] + res + [s[j]]
    else:
        c1, res1 = find_LPS(s, i + 1, j)
        c2, res2 = find_LPS(s, i, j - 1)
        if c1 > c2:
            return c1, res1
        else:
            return c2, res2


# string combination method
def find_LPS2(s, idx, st, res):
    global max_lps
    for i in range(st, len(s)):
        res[idx] = s[i]
        sub_str = res[:idx]
        if sub_str == sub_str[::-1] and len(max_lps) < len(sub_str):
            max_lps = sub_str
        # check LPS
        find_LPS2(s, idx+1, i+1, res)


s = "character"
print(find_LPS3(s, 0, len(s)-1))
#
# res = [''] * len(s)
# max_lps = ''
# find_LPS2(s, 0, 0, res)
# print(max_lps)

# print(find_LPS(s, 0, len(s)-1))
