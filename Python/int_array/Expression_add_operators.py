'''
given a string that contains only digits 0-9 and a target value, return all posibilities to add binary
operators "+, -, *" between the digits so they evaluate to the target value

input: "123", target = 6
output: ["1+2+3", "1*2*3"]

input: "00", target = 0
output: ["0+0", "0-0", "0*0"]
'''

import copy


def find_combinations(a, n, st=0, res=[], final_res=[]):
    if st >= n:
        final_res.append(copy.deepcopy(res))
        return

    for idx in range(st+1, n+1):
        res.append(a[st:idx])
        find_combinations(a, n, idx, res, final_res)
        del res[len(res)-1]
    return final_res


# res = ["1", '', "2", '', "3"]
def create_expression(arr, target, res, final_res, idx=0):
    if idx+1 >= len(arr):
        expr = ''.join(res)
        if eval(expr) == target:
            final_res.append(expr)
        return
    for operator in ["+", "-", "*"]:
        res[2 * idx + 1] = operator
        create_expression(arr, target, res, final_res, idx+1)


def evaluate_target(a, target):
    if not a or len(a) <= 1:
        return []
    res = find_combinations(a, len(a))
    final_res = []
    for item in res:
        if len(item) == 1:
            continue
        candidate = []
        for idx, v in enumerate(item):
            candidate.append(str(int(v)))
            if idx < len(item)-1:
                candidate.append('')
        create_expression(item, target, candidate, final_res)
    return final_res


a="1204"
print(evaluate_target(a, 6))