'''
give k sorted arrays, and merge them into one array
a = [
[1,4,5,7],
[1,3,6,8],
[2,5]
]
min_heap:
(1,0), (1,1), (2,2) -> (1,0)
(1,1),(2,2),(4,0) -> (1,1)
(2,2),(4,0), (3,1) -> (2,2)
(3,1) (5,2) (4,0) -> (3,1)
(4,0) (6,1) (5,2) -> (4,0)

edge cases:
a = [
[1,4,5,7],
[],
[2,5]
]
a = [
[],
[],
[]
]
'''


import heapq


def sort_arrays(a):
    k = len(a)
    print(f"total arrays: {k}")
    m_heap, res = [], []
    for idx, arr in enumerate(a):
        if len(arr) > 0:
            heapq.heappush(m_heap, (arr[0], idx, 0))

    while(len(m_heap) > 0):
        v, arr_idx, idx = heapq.heappop(m_heap)
        res += [v]
        if idx + 1 >= len(a[arr_idx]):
            k -= 1
            # TODO: check if only one array left
            continue
        heapq.heappush(m_heap, (a[arr_idx][idx+1], arr_idx, idx+1))

    return res

a = [
[1,4,5,7,9,11],
[1,3,6,8],
[2,5]
]
print(sort_arrays(a))
