'''
Given two strings, identify all palindromes that can be formed from each string's letters. Select one palindrome from each set that, when combined and rearranged, creates the longest possible palindrome. If multiple palindromes of this maximum length exist, return the alphabetically smallest one.
Example
s1 = 'aabbc'
s2 = 'ddefefq'
All of the letters of the first string can make a palindrome.
The choices using all letters are [abcba, bacab].

All of the letters of the second string can make a palindrome.
The choices using all letters are [defqfed, dfeqefd, edfqfde, efdqdfe, fdeqedf, fedqdef].
The two longest results in s1 have a length of 5.
The six longest results in s2 have a length of 6.

From the longest results for s1 and s2, merge the two that form the lowest merged
palindrome, alphabetically.
In this case, choose abcba and defqfed.
The two palindromes can be combined to form a single palindrome
if either the c or the q is discarded.
The alphabetically smallest combined palindrome is abdefcfedba.
'''

'''
solution:
s1: create ht1 with char:cnt --> from 'a' to 'z' --> keep the first item with odd cnt --> update following items with odd cnt with cnt-1
    a:3, b:2, c:3, d:1 --> a:3, b:2, c:2
s2: create ht2 with char:cnt
    a:1: c:2, d:5 --> a:1: c:2, d:4 
    
--> from 'a' to 'z' --> merge ht1 & ht2 --> keep the first time with odd cnt (cnt1+cnt2)
'''


def generate_ht(s, ht):
    for c in s:
        if c in ht:
            ht[c] += 1
        else:
            ht[c] = 1
    found_odd = False
    for c1 in range(ord('a'), ord('z')+1, 1):
        s1 = chr(c1)
        if s1 in ht:
            if ht[s1] % 2 == 1:
                if found_odd:
                    ht[s1] -= 1
                    if ht[s1] == 0:
                        del ht[s1]
                else:
                    found_odd = True


def merge_ht(ht1, ht2):
    found_odd = False
    for c in range(ord('a'), ord('z')+1, 1):
        s = chr(c)
        cnt1 = ht1[s] if s in ht1 else 0
        cnt2 = ht2[s] if s in ht2 else 0
        cnt = cnt1 + cnt2
        if cnt > 0:
            if cnt % 2 == 1:
                if found_odd:
                    cnt -= 1
                    if cnt == 0:
                        if s in ht1:
                            del ht1[s]
                        continue
                else:
                    found_odd = True
            ht1[s] = cnt


def generate_palindrome(ht):
    f_h, s_c, found_odd = "", "", False
    for c in range(ord('a'), ord('z')+1, 1):
        s = chr(c)
        if s in ht:
            cnt = ht[s]
            if ht[s] % 2 == 1:
                if found_odd:
                    cnt -= 1
                else:
                    found_odd = True
                    s_c = s
            for _ in range(0, cnt // 2):
                 f_h += s

    return f_h + s_c + f_h[::-1]


def merge_palindromes(s1, s2):
    ht1, ht2 = dict(), dict()
    generate_ht(s1, ht1)
    generate_ht(s2, ht2)
    merge_ht(ht1, ht2)
    return generate_palindrome(ht1)


print(merge_palindromes("aabbc", "ddefefq"))