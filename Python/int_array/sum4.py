# given an integer n, and integer array, find all unique arrays of 4 elements that sums to n
# e.g., a = [2, 5, -3, 4, -2, 1, 0], n = 3
# resput: [2, -3, 4, 0], [5, -3, 1, 0], [4, -2, 1, 0]


def sum4(a, n, res, st, idx):
    global complexity
    # print(f"res={res}, st={st}")
    if st == 4:
        print(res)
        # if sum(res) == n:
        #     print(res)
        return
    if idx >= len(a):
        return
    complexity += 1
    res[st] = a[idx]
    # if 4 - st <= len(a) - idx:
    sum4(a, n, res, st+1, idx + 1) # take a[idx] to res[st]
    # if 4 - st <= len(a) - idx - 1:
    sum4(a, n, res, st, idx + 1)  # take a[idx + 1] to res[st]

a = [2, 5, -3, 4]
complexity = 0
n = 3
res = [0, 0, 0, 0]
sum4(a, n, res, 0, 0)
print(f"{complexity}")
