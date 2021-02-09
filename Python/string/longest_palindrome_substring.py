# given a string, find the longest substring which is palindrome
# s = "abstcacta", return "tcact"
#
max_len = 0
steps = 0
finished = set()


def key(l, r):
    return "{}:{}".format(l, r)


def find_palindrome(s, l, r, c):
    global steps, max_len, finished
    if max_len > r - l or key(l,r) in finished or r >= len(s) or l >= r or \
            l < 0 or r < 0:
        finished.add(key(l,r))
        return
    steps += 1
    print "{} : {} - steps: {}".format(l, r, steps)
    # pay attention to special case: "aa" is palindrome
    if s[l] == s[r] and (c[(l+1, r-1)] or r - l == 1):
        c[(l, r)] = True
        finished.add(key(l,r))
        max_len = max(r - l + 1, max_len)
    else:
        find_palindrome(s, l+1, r, c)
        finished.add(key(l+1, r))
        find_palindrome(s, l, r-1, c)
        finished.add(key(l, r-1))


c = dict()
# s = "abstcacta"
s = "astaa"
for i in range(0, len(s)):
    for j in range(0, len(s)):
        if i == j:
            c[(i, j)] = True
        else:
            c[(i, j)] = False

find_palindrome(s, 0, len(s)-1, c)

print "max len = {}".format(max_len)
