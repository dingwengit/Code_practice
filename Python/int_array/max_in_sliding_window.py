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

class item_class:
    def __init__(self, v, removed=False):
        self.v, self.removed = (-1)*v, removed

    def __gt__(self, other):
        return self.v > other.v


def max_in_sliding_window(a, k):
    if len(a) < k or k <= 0:
        return None

    res, window, h = [], [], []

    for i in range(k):
        item = item_class(a[i])
        window.append(item)
        heapq.heappush(h, item)
    res.append(h[0].v * (-1))
    item = window.pop(0)
    item.removed = True
    idx = k
    while idx < len(a):
        item = item_class(a[idx])
        window.append(item)
        heapq.heappush(h, item)
        # get the max value from heap
        while h[0].removed:
            heapq.heappop(h)
        res.append(h[0].v * (-1))
        item = window.pop(0)
        item.removed = True
        idx += 1

    return res

a = [2, -1, 8, 1, 6, 3, 5, 4]
print(max_in_sliding_window(a, 3))