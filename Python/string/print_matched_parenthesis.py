# give N pairs of "(", ")", print out all possible matched parenthesis
# e.g., N = 3, result: ((())), ()()(), (()()), ()(()), ...
# given pos (i)
# how many lc, rc?
# hint : don't use arraylist as result, use idx and fixed size array


def find_matched_parenthesis(n, res, idx=0, lp=0, rp=0):
    if idx >= 2 * n:
        print(f"{''.join(res)}")

    if lp < n:
        res[idx] = '('
        find_matched_parenthesis(n, res, idx+1, lp+1, rp)
    if rp < lp:
        res[idx] = ')'
        find_matched_parenthesis(n, res, idx+1, lp, rp+1)

res = [''] * (2 * n)
find_matched_parenthesis(3, res)
