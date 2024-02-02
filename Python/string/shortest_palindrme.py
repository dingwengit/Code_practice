'''
give a string S, you are allowed to add characters to convert it to a palindrome, write function to find out the shortest
palindrome you can convert it to

input: "aaba"
ouput: "aabaa"

input: "abcd"
output: "dcbabcd" or "abcdcba"

solution:
(1) find out what are minimum cuts that converts a string into palindrones
(2) "aaba" -> ['a', 'aba'] then the result would be ['a', 'aba', 'a']
              [a, aba, xyx, cdc] then the result would be [a, aba, xyx, cdc, xyx, aba, a]
'''

import sys, copy

min_cuts = sys.maxsize
final_res = []

def convert_palindrome(s):
    def get_minimum_palindromes(s, st=0, res=[]):
        global min_cuts, final_res
        if st >= len(s):
            if len(res) < min_cuts:
                min_cuts = len(res)
                final_res = copy.deepcopy(res)
                print(final_res)
            return
        for idx in range(st+1, len(s)+1):
            prefix = s[st:idx]
            if prefix == prefix[::-1]:
                res.append(prefix)
                get_minimum_palindromes(s, idx, res)
                del res[len(res)-1]


    if not s or len(s) < 1:
        return None
    get_minimum_palindromes(s)

    if len(final_res) == 1:
        return final_res[0]
    print(f"final_res:{final_res}")
    final_s = s
    if len(final_res[0]) > len(final_res[len(final_res)-1]):
        for i in range(1, len(final_res)):
            final_s = final_res[i][::-1] + final_s
    else:
        for i in range(len(final_res)-2, -1, -1):
            final_s += final_res[i][::-1]
    return final_s

s="abbaecd"
print(convert_palindrome(s))