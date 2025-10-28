'''
Given an array of integers nums, perform k operations to
minimize the sum of the elements. Each operation consists of:

    Removing an element from the array
    Dividing it by 2
    Inserting the ceiling of the result back into the array

Return the minimum possible sum after k operations.



Example 1

Input: n = 3 elements, nums = [10, 20, 7], k = 4

Output: 14

Explanation:

    The ceiling of 7/2 = 4 → [10, 20, 4]
    The ceiling of 10/2 = 5 → [5, 20, 4]
    The ceiling of 20/2 = 10 and 10/2 = 5→ [5, 5, 4]
    The sum of the final array is 5 + 5 + 4 = 14.

Example 2

Input: n = 2 elements, nums = [2, 3], k = 1

Output: 4

Explanation: Whether we choose 2 or 3, the answer is the same.

    The ceiling of 2/2 = 1, 1 + 3 = 4
    The ceiling of 3/2 = 2, 2 + 2 = 4
'''

import heapq

def find_min(arr, k):
    if len(arr) == 0:
        return 0
    if k <= 0:
        return sum(arr)

    hp = []

    for a in arr:
        heapq.heappush(hp, -1 * a) # we need max_heap

    for _ in range(k):
        v = heapq.heappop(hp)
        heapq.heappush(hp, v // 2)

    return -1 * sum(hp)

print(find_min([10, 20, 7], 4))
print(find_min([2, 3], 1))