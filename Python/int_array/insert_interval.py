'''
given a set of non-overlapping intervals,
insert a new interval into the intervals,
assume that the intervals were initially sorted acoording to  their start times

Input: [[1,3],[6,9]], insert: [4,6]
      ---
            ---
       ----
idx   1 2 3 4 6 7 8 9
st:0  1   0 4 4 4 4 0
end:0 3   0 5 9 9 9 0
output: [1,5], [6,9]

Input: [[6,7],[8,9] [12,18]], insert: [2,8]
output: [2,9], [12,18]
'''

def insert_interval(a, ins):
    idx = min(a[0][0], ins[0])
    idx_a, st, end, res, found_ins = 0,idx,0, [], False

    while (idx >= 0):
        if idx_a < len(a) and a[idx_a][0] == idx:
            if st == 0:
                st = a[idx_a][0]
            end = max(end, a[idx_a][1])
        if ins[0] == idx:
            if st == 0:
                st = ins[0]
            end = max(end, ins[1])
        if idx == ins[1]:
            found_ins = True
        if idx_a < len(a) and idx == a[idx_a][1]:
            idx_a += 1
        if idx == end:
            res.append((st, end))
            st, end = 0, 0
            if found_ins:
                break
        idx += 1
    res += a[idx_a:]
    return res

a, insert = [(10,13),(16,19)], [21,25]
print(insert_interval(a, insert))