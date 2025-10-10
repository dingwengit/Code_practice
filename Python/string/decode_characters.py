#
# given encoded string -- 2(3(b2(ax)4(c))5(x))
# output a string -- "baaccccbaaccccbaacccc"
# stack: [(2,0), (3,0), (2, 1)
# cur_idx:3
# res: ["b", "a", "x", "cccc", "x"]
# edge case: a
# invalid input: 3(b2()((), 33(b2(a))
#


def decode_str(s):
    stack, res, idx = [], [], 0
    for c in s:
        if c >= 'a' and c <= 'z':
            res.append(c)
            idx += 1
        if c >= '1' and c <= '9':
            stack.append((int(c), idx))
        if c == '(':
            continue
        if c == ')':
            cnt, idx2 = stack.pop()
            # print(f"res={res}, idx2={idx2}, idx={idx}")
            res2 = res[idx2:idx] * cnt
            # print(f"res2={res2}")
            for _ in range(idx2+1, idx):
                res.pop()
                idx -= 1
            res[-1] = "".join(res2)
    return "".join(res)

s = "3(b2(xyz)4(c))"
# s = "abc2(xb4(d))"
print(decode_str(s))
