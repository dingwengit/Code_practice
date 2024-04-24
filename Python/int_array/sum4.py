# given an integer n, and integer array, find all unique arrays of 4 elements that sums to n
# e.g., a = [2, 5, -3, 4, -2, 1, 0], n = 3
# output: [2, -3, 4, 0], [5, -3, 1, 0], [4, -2, 1, 0]

def sum4(a, n, out, st, idx):
    if st == 4:
        # print(out)
        if sum(out) == n:
            print(out)
        return
    if idx >= len(a):
        return

    out[st] = a[idx]
    sum4(a, n, out, st+1, idx + 1)
    sum4(a, n, out, st, idx + 1)

a = [2, 5, -3, 4, -2, 1, 0]
n = 3
out = [0, 0, 0, 0]
sum4(a, n, out, 0, 0)
