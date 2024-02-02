#
# given encoded string -- 3(b2(a)4(c))
# output a string -- "baaccccbaaccccbaacccc"
# edge case: a
# invalid input: 3(b2()((), 33(b2(a))
#
import copy


# 1. when to reset cur = []
# 2. when to add to res (when stack is empty!)


def decode_str(s):
    idx, stack, res, cur = 0, [], [], []

    while idx < len(s):
        if s[idx].isnumeric() and s[idx] != '0':
            stack.append((int(s[idx]), copy.deepcopy(cur))) # note that we need remember both cnt & cur list
            if s[idx+1] != "(":
                raise Exception("invalid input - no ( found after a digit")
            idx += 1
            cur = []
        elif s[idx] == ")":
            if len(stack) == 0:
                raise Exception("Invalid input with extra )")
            cnt, l_str = stack.pop()
            for _ in range(cnt):
                l_str.append(''.join(cur))
            cur = l_str
            if len(stack) == 0:
                res.append(''.join(l_str))
                cur = []
        else:
            if len(stack) == 0:
                res.append(s[idx])
                cur = []
            else:
                cur.append(s[idx])
        print(f"idx: {idx}, cur: {cur}")
        idx += 1

    print(f"res: {res}")
    return ''.join(res)

s = "3(b2(a)4(c))"
s = "abc2(xb4(d))"
print(decode_str(s))
