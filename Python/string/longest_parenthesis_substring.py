#!/usr/bin/env python

'''
given a string consists of only "(" and ")", find out the longest well-formed parenthesis substring

input: )(()())
output: 6 (()())
'''


# Solution 1  - O(n ^ 2)

def check_valid_str(s):
    stack = []
    for c in s:
        if c == "(":
            stack.append(c)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False


def find_max_substr(s, st, end):
    if end - st <= 1:
        if s[end] == "(" and s[st] == ")":
            return 2
        else:
            return 0

    if check_valid_str(s[st:end+1]):
        return end - st + 1
    else:
        return max(find_max_substr(s, st+1, end), find_max_substr(s, st, end-1))

s = "()()(()))"
print(find_max_substr(s, 0, len(s)-1))

# Solution 2 -- O(n)
def find_max_parenthesis_substr(s):
    stack = []
    cnt, max_cnt = 0, 0

    for c in s:
        if c == "(":
            stack.append(cnt)
            cnt = 0
        else:
            if len(stack) == 0:
                cnt = 0
            else:
                cnt += stack.pop() + 2
                max_cnt = max(max_cnt, cnt)
    return max_cnt

print(find_max_parenthesis_substr(s))
