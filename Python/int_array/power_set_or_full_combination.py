# input: [0,1,2]
# output: [None, [0], [1], [2], [0,1],[0,2], [1,2], [0,1,2]]

def power_set(a, cur_res, st=0, k=0, ):
    for i in range(st, len(a)):
        cur_res[k] = a[i]
        print(cur_res[:k+1])
        # res.append(copy.deepcopy(cur_res[:k+1]))
        power_set(a, cur_res, i+1, k+1)


a = [0,1,2]
cur_res = [''] * len(a)
power_set(a, cur_res)
