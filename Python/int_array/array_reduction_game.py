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

arr = [2, 5, 3, 3, 4, 6]
sum = 19

s = 7 (3,4) with idx (2,4)
s = 7 (3,4) with idx (3,4)
s = 7 (2,5) with idx (0,1)
s = 7 (3,6) with idx (2,5)
s = 7 (3,6) with idx (3,5)
s = 6 (2,4) with idx (0,4)
s = 6 (5,3) with idx (1,2)
s = 6 (5,3) with idx (1,3)
s = 4 (2,6) with idx (0,5)
s = 3 (5,6) with idx (1,5)
s = 2 (4,6) with idx (4,5)
s = 1 (2,3) with idx (0,2)
s = 1 (2,3) with idx (0,3)
s = 1 (5,4) with idx (1,4)
'''
max_xor_sum = 0
max_xor_res = []

def generate_s_tripples(arr, s_tripples):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            val = arr[i] ^ arr[j]
            ins_idx = len(s_tripples)
            for idx, t in enumerate(s_tripples):
                if val >= t[2]:
                    ins_idx = idx
                    break;
            s_tripples.insert(ins_idx, (i, j, val))

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

        if len(res) < n - 1:
            red_idx_set.add(s_tripples[idx][1])
            find_max_xor(s_tripples, n, res, idx+1, red_idx_set)
            red_idx_set.remove(s_tripples[idx][1])
        del res[len(res)-1]

arr = [2, 5, 3, 3, 4, 7]
# arr = [3, 2, 1]
res = []
s_tripples = []
generate_s_tripples(arr, s_tripples)
print(s_tripples)
find_max_xor(s_tripples, len(arr), res, 0, set())
print(max_xor_sum)
print(max_xor_res)