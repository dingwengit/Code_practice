'''
given integer array, find the max value of a sliding window (size = k)

input: a=[2, -1, 3, 1, 6, 9, 5, 4], k = 3
output:
 [(2, -1, 3), 1, 6, 9, 5, 4] -> 3
 [2, (-1, 3, 1), 6, 9, 5, 4] -> 3
 [2, -1, (3, 1, 6), 9, 5, 4] -> 6
 [2, -1, 3, (1, 6, 9), 5, 4] -> 9
 [2, -1, 3, 1, (6, 9, 5), 4] -> 9
 [2, -1, 3, 1, 6, (9, 5, 4)] -> 9
 output array: [3,3,6,9,9,9]

 let's do it in O(n) complexity
'''

import heapq

class item:
    def __init__(self, v, idx):
        self.v, self.idx = -1 * v, idx
    def __gt__(self, other):
        return self.v > other.v

def max_in_sliding_window(a, k):
    if k <= 1 or k > len(a):
        return a
    res, hp = [], []
    for i in range(k):
        heapq.heappush(hp, item(a[i], i))
    j = k
    res.append(-1 * hp[0].v)
    remove_idx = 0
    while (j < len(a)):
        heapq.heappush(hp, item(a[j], j))
        x = hp[0]
        while (x.idx <= remove_idx):
            x = heapq.heappop(hp)
        res.append(-1 * x.v)
        j += 1
        remove_idx += 1
    return res

a = [8, -1, 2, 1, 6, 3, 5, 4]
print(max_in_sliding_window(a, 3))