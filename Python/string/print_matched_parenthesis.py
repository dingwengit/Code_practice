# give N pairs of "(", ")", print out all possible matched parenthesis
# e.g., N = 3, result: ((())), ()()(), (()()), ()(()), ...
# given pos (i)
# how many lc, rc?
# hint : don't use arraylist as result, use idx and fixed size array

def get_lc_rc(s):
    lc, rc = 0, 0
    for c in s:
        if c == '(':
            lc += 1
        if c == ')':
            rc += 1
    return lc, rc

def find_matched_p(n, idx, res):
    if 2 * n <= idx:
        print ''.join(res)
        return
    # print "idx: {} res: {}".format(idx, res)
    lc, rc = get_lc_rc(res[:idx])
    if lc < n:
        res[idx] = '('
        find_matched_p(n, idx+1, res)
    if rc < lc:
        res[idx] = ')'
        find_matched_p(n, idx+1, res)


def find_matched_p2(n, idx, lc, rc, res):
    if 2 * n <= idx:
        print ''.join(res)
        return
    if lc < n:
        res[idx] = '('
        find_matched_p2(n, idx+1, lc+1, rc,  res)
    if rc < lc:
        res[idx] = ')'
        find_matched_p2(n, idx+1, lc, rc + 1, res)

n = 3
res = [' '] * (2 * n)
find_matched_p2(n, 0, 0, 0, res)
# find_matched_p(n, 0, res)
