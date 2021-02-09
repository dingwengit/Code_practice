# input: [0,1,2]
# output: [None, [0], [1], [2], [0,1],[0,2], [1,2], [0,1,2]]
import copy


def power_set(a, st, k, cur_res, res):
    for i in range(st, len(a)):
        cur_res[k] = a[i]
        res.append(copy.deepcopy(cur_res[:k+1]))
        power_set(a, i+1, k+1, cur_res, res)


a = [0,1,2]
res = [None]
cur_res = [''] * len(a)
power_set(a, 0, 0, cur_res, res)
print res
