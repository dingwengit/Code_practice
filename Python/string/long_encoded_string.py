# Given a string composed solely of lowercase English letters (a-z), the following encoding rules are used to convert its characters into a string s:
#
#     'a' is represented as 1, 'b' as 2, 'c' as 3, up to 'i' which is represented as 9
#     'j' is represented as 10#, 'k' as 11#, 'l' as 12#, up to 'z' which is represented as 26#
#     If a character repeats consecutively two or more times, its count is indicated in parentheses following the encoded character, e.g., 'aa' is encoded as '1(2)'
#
# Given an encoded string s, determine the character counts for each letter of the original, decoded string.  Return an array of 26 integers where index 0 contains the number of 'a's, index 1 contains the number of 'b's, and so on.
#
#
#
# Examples
#
#     s = "1226#24#", decoded = "abzx"
#     s = "1(2)23(3)", decoded = "aabccc"
#     s = "2110#(2)", decoded = "bajj"
#     s = "23#(2)24#25#26#23#(3)", decoded = "wwxyzwww"
#
#   The answer arrays for each string are shown.
#
# [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1] "abzx"
# [2, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] "aabccc"
# [1, 1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] "bajj"
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 1, 1, 1] "wwxyzwww"
#
#
#
# Function Description
#
# Complete the frequency function in the editor below.
#
#
#
# frequency has the following parameter:
#
#     string s: an encoded string
#
#
#
# Return
#
#     int[26]: the character frequencies as described

def long_endocded_string(s, arr):
    idx = 0
    while idx < len(s):
        cnt = 1
        s1 = s[idx]
        if s[idx + 2] == '#':
            s1 = s[idx:idx+2]
            idx += 2
        if idx + 1 < len(s) and s[idx + 1] == "(":
            idx += 1
            cnt = int(s[idx+1:idx+2]) # note that count is < 10
            idx += 2
        arr[int(s1)-1] += cnt
        idx += 1

arr = [0] * 26
long_endocded_string("1226#24#", arr)
print(arr)
arr = [0] * 26
long_endocded_string("1(2)23(3)", arr)
print(arr)
arr = [0] * 26
long_endocded_string("2110#(2)", arr)
print(arr)
arr = [0] * 26
long_endocded_string("23#(2)24#25#26#23#(3)", arr)
print(arr)