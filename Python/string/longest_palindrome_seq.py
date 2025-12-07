# problem : for input "character",
# the longest palindrome subsequence is "carac"

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
def find_LPS(s, i, j, ht=dict()):
    key=f"{i}-{j}"
    if key in ht:
        return ht[key]
    if i == j:
        ht[key] = 1, [s[i]]
        return ht[key]

    if i + 1 == j and s[i] == s[j]:
        ht[key] = 2, [s[i], s[j]]
        return ht[key]

    if s[i] == s[j]:
        c, res = find_LPS(s, i+1, j-1)
        ht[key] = c + 2, [s[i]] + res + [s[j]]
        return ht[key]
    else:
        c1, res1 = find_LPS(s, i + 1, j)
        c2, res2 = find_LPS(s, i, j - 1)
        if c1 > c2:
            ht[key] = c1, res1
            return ht[key]
        else:
            ht[key] = c2, res2
            return ht[key]

s = "acharactera"
# print(find_LPS3(s, 0, len(s)-1))
#
# res = [''] * len(s)
# max_lps = ''
# find_LPS2(s, 0, 0, res)
# print(max_lps)

print(find_LPS(s, 0, len(s)-1))
