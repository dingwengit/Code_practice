'''
# given a string, find the longest substring which is palindrome
# s = "abstcacta", return "tcact"
(a)(b)(s)(t)(c)(a)(c)(t)(a)
(ab)(bs)(st)(tc)...
(abs)(bst)...
#
'''
max_len = 0

def find_longest_palindrome(s, st, end):
    substr = s[st:end]
    if substr == substr[::-1]:
        return len(substr)
    else:
        return max(find_longest_palindrome(s, st+1, end), find_longest_palindrome(s, st, end-1))


def find_LPSub(s, st=0, res=[]):
    global max_len
    if st >= len(s):
        # print(res)
        return
    for idx in range(st+1, len(s)+1):
        prefix = s[st:idx]
        if prefix == prefix[::-1]:
            max_len = max(max_len, idx - st)
            res.append(prefix)
            find_LPSub(s, idx)
            del res[len(res)-1]

# steps = 0
# finished = set()
#
#
# def key(l, r):
#     return "{}:{}".format(l, r)
#
#
# def find_palindrome(s, l, r, c):
#     global steps, max_len, finished
#     if max_len > r - l or key(l,r) in finished or r >= len(s) or l >= r or \
#             l < 0 or r < 0:
#         finished.add(key(l,r))
#         return
#     steps += 1
#     print "{} : {} - steps: {}".format(l, r, steps)
#     # pay attention to special case: "aa" is palindrome
#     if s[l] == s[r] and (c[(l+1, r-1)] or r - l == 1):
#         c[(l, r)] = True
#         finished.add(key(l,r))
#         max_len = max(r - l + 1, max_len)
#     else:
#         find_palindrome(s, l+1, r, c)
#         finished.add(key(l+1, r))
#         find_palindrome(s, l, r-1, c)
#         finished.add(key(l, r-1))
#
#
# c = dict()
# # s = "abstcacta"
# s = "astaa"
# for i in range(0, len(s)):
#     for j in range(0, len(s)):
#         if i == j:
#             c[(i, j)] = True
#         else:
#             c[(i, j)] = False
#
# find_palindrome(s, 0, len(s)-1, c)
# s = "abstcactastcacts"
# s = "abcb"
find_LPSub(s)
print("max len = {}".format(max_len))
print("max_len: {}".format(find_longest_palindrome(s, 0, len(s))))



