# Given an array arr[] of size n containing integers. The problem is to find
# the length of the longest sub-array having sum equal to the given value k.
#
# Input : arr[] = { 10, 5, 2, 7, 1, 9 },
#             k = 15
# Output : 4
# The sub-array is {5, 2, 7, 1}
#              { 10,         5,            2,   7,    1,     15 }
# dict           10:1       15:2          17:3   24:4  25:5  40:6
# max_len:0                 2                          4
# sum - k in dict                                    25-15=10


def find_LSA(arr, k):
    cur_sum, max_len, dic = 0, 0, dict()
    for i in range(len(arr)):
        cur_sum += arr[i]
        # 1. sum not in dict
        if cur_sum not in dic:
            dic[cur_sum] = i
        # 2. sum == k
        if cur_sum == k:
            max_len = max(max_len, i + 1)
        # 3. cur_sum - k in dict
        if cur_sum - k in dic:
            max_len = max(max_len, i - dic[cur_sum - k])
    return max_len

print(find_LSA([10, 5, 2, 7, 1, 9], 15))
