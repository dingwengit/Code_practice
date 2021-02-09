# given s = "abc", print its permutation
# "abc", "bac", "bca", ...

def str_permutation(s, idx):
    if idx >= len(s):
        print ''.join(s)
    for i in range(idx, len(s)):
        if i != idx:
            s[idx], s[i] = s[i], s[idx]
        str_permutation(s, idx + 1)
        if i != idx:
            s[idx], s[i] = s[i], s[idx]


s = ["a", "b", "c"]
str_permutation(s, 0)