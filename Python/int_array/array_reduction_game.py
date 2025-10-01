'''
In a new game, players must maximize their score by performing operations on an integer array until its length is reduced to one. Starting with a score of zero, players must execute exactly n-1 operations.

Each operation:
    Decreases the array length by one
    Requires selecting two indices x and y (where 1 ≤ x, y ≤ n)
    Adds arr[x] ⊕ arr[y] to the score (where ⊕ represents bitwise XOR)
    Removes either arr[x] or arr[y] from the array
Return the highest possible score achievable through optimal operations.

Example
n = 3,
arr = [3, 2, 1]
Expected Output: 5
An optimal method:
1. Choose index 2 and 3, remove the 2nd index, score = arr[2] ⊕ arr[3] = 2 ⊕ 1 = 3, arr = [3, 1].
2. Choose index 1 and 2, remove the 1st index, score = arr[1] ⊕ arr[2] = 3 ⊕ 1 = 2, arr = [1].
Sum the results and return the total score, 3+2 = 5.

'''
max_xor_sum = 0
max_xor_res = []

def generate_s_tripples(arr, s_tripples):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            val = arr[i] ^ arr[j]
            s_tripples.append((i, j, val))
    # sort the array based on index 2 of tripple
    s_tripples.sort(reverse=True, key=lambda x: x[2])


def find_max_xor(s_tripples, n, res, idx, red_idx_set):
    global max_xor_res, max_xor_sum
    if idx >= len(s_tripples):
        return
    if len(res) >= n - 1:
        cur_sum = sum([r[2] for r in res])
        if cur_sum > max_xor_sum:
            max_xor_sum = cur_sum
            max_xor_res = res.copy()
        return

    if s_tripples[idx][0] in red_idx_set or s_tripples[idx][1] in red_idx_set:
        find_max_xor(s_tripples, n, res, idx+1, red_idx_set)
    else:
        res.append(s_tripples[idx])
        red_idx_set.add(s_tripples[idx][0])
        find_max_xor(s_tripples, n, res, idx+1, red_idx_set)
        red_idx_set.remove(s_tripples[idx][0])
        # print(f"red_idx_set={red_idx_set}, res={res}, idx={idx}")

        if len(res) < n - 1: # if this is the last pair, we don't need to choose which letter to drop
            red_idx_set.add(s_tripples[idx][1])
            find_max_xor(s_tripples, n, res, idx+1, red_idx_set)
            red_idx_set.remove(s_tripples[idx][1])
        del res[len(res)-1]

arr = [2, 5, 3, 3]
# arr = [2, 3, 4, 7, 5, 3]
# arr = [3, 2, 1]
res = []
s_tripples = []
generate_s_tripples(arr, s_tripples)
print(s_tripples)
find_max_xor(s_tripples, len(arr), res, 0, set())
print(max_xor_sum)
for i, v in enumerate(max_xor_res):
    max_xor_res[i] = (arr[v[0]], arr[v[1]], v[2])
print(max_xor_res)