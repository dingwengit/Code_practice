# given string = "abcdef", and pattern = "*c*e", with wild_char as "*",
# where it matches
# return true or false, if they match or not
# case 1: "abc", "a*"
# case 2: "abc", "*ab"
# case 3: "abc", "*abcd"
# case 4: "", "*"
# case 5: "", "***"


def isMatch(str, s_idx,  p, p_idx):
    if not str and not p:
        return True

    if p[p_idx] != '*':
        if s_idx >= len(str) or p[p_idx] != str[s_idx]: # if end of str,
            # still have char in pattern with non-wild-char
            return False
        if p_idx + 1 < len(p): # this char matches, move to next
            return isMatch(str, s_idx + 1, p, p_idx + 1)
        elif s_idx + 1 == len(str): # both str and pattern reached the end
            return True
        return False
    elif p_idx + 1 == len(p): # the last char is '*' in pattern
        return True
    else: # now we allow each char in str to take this place, and compare to
        # next char in pattern, if any of them matches, we are good
        if s_idx == len(str): # if no more str, but has char in pattern
            return isMatch(str, s_idx, p, p_idx + 1)
        match = False
        for i in range(s_idx, len(str)):
            if isMatch(str, i, p, p_idx + 1):
                match = True
                break # this is to improve performance
        return match
    return False

print(isMatch("abcdcbcb", 0, "*a*b*cb*c*b", 0))
