'''
given a set of non-overlapping intervals, insert a new interval into the intervals, assume that the intervals were initially sorted acoording to  their start times

Input: [[1,3],[6,9]], insert: [2,5]
output: [1,5], [6,9]

Input: [[6,7],[8,9]], insert: [2,8]
st = 2
output: [2,9]
'''


def insert_interval(a, insert):
    st, end = insert
    found_st, found_end = False, False
    res = []
    for item in a:
        if not found_st:
            # case 1
            if st < a[0][0]:
                found_st = True
            # case 2
            if st >= item[0] and st <= item[1]:
                st = item[0]
                found_st = True
            # case 3
            if st < item[0]:
                found_st = True
        if found_st and not found_end:
            # case 1
            if end < a[0][0]:
                found_end = True
                res = [[st, end]]
                res += a
                break
            # case 2
            if end >= item[0] and end <= item[1]:
                end = item[1]
                found_end = True
                res.append([st, end])
                continue
            # case 3
            if end < item[0]:
                found_end = True
                res.append([st, end])
        # case 1
        if not found_st:
            res.append(item)
            continue
        # case 2
        if not found_end:
            continue
        # case 3
        res.append(item)

    # case 1
    if not found_st and not found_end:
        return a + [[st, end]]
    # case 2
    if not found_end:
        return res + [[st, end]]
    # case 3
    return res

a, insert = [[10,13],[16,19]], [11,16]
print(insert_interval(a, insert))