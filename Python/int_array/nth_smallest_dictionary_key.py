'''
Complete a function that returns the smallest key(sorted in ascending order
alphabetically) of the given input dictionary containing nth hgihest value
dictionary: {'e': 1, 'b': 2, 'c': 100, 'd': 30, 'a': 30}, n : 2 (2nd highest
value)

min_heap (size=n):
n=2
['e': 1
 'b': 2]

'c': 100

['b': 2
 'c': 100]

'd': 30

['d': 30
 'c': 100]

'a': 30

['a': 30
 'c': 100]

input: dic, n
output: char_key which hold the nth highest value
'''

import heapq


def find_nth_highest(dic, n):
    heap = []

    for k, v in dic.items():
        if len(heap) < n:
            heapq.heappush(heap, (v, k))
        else:
            if heap[0][0] == v:
                if heap[0][1] > k:
                    heap[0] = heap[0][0], k
            else:
                heapq.heappushpop(heap, (v,k))
    return (heap[0][1], heap[0][0])


dic = {'e': 1, 'b': 2, 'c': 100, 'd': 30, 'a': 30}

print(find_nth_highest(dic, 2))