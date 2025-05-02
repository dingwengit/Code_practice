# given street blocks with some attributes, find a block which has shortest
# distance of given set of attributes are True
# for example:
"""
input_blocks = [
{"gym":False, "grocery_store":True, "office":False},
{"gym":False, "grocery_store":True, "office":False},
{"gym":True, "grocery_store":False, "office":False},
{"gym":False, "grocery_store":True, "office":True},
{"gym":False, "grocery_store":False, "office":True},
{"gym":True, "grocery_store":False, "office":False}
]
block_idx: 0 -- 1 -- 2 -- 3 -- 4 -- 5
Solution 1
-- search range x from 1 to len(a)-1 --> [0,1,2,3,4,5] --> [(0,1),(1,2),(2,3),(3,4),(4,5)] --> [(0,1,2),(1,2,3),(2,3,4),(3,4,5)]--> [(0,1,2,3,4),(1,2,3,4,5)]
-- final distance = x / 2, so why not use search range in odd number: 1, 3, 5

Assumption: the following 2 cases has the same distance value as 1
case 1
{"gym":True, "grocery_store":False, "office":False}, <-- live here
{"gym":False, "grocery_store":True, "office":True},
case 2
{"gym":False, "grocery_store":False, "office":True},
{"gym":True, "grocery_store":False, "office":False},  <-- live here
{"gym":False, "grocery_store":True, "office":False},

block_idx: 0 -- 1 -- 2 -- 3 -- 4 -- 5
search_range = min(len(blocks)-1, cur_min_distance)

Solution 2
             (0, 1, 0), (1, 0, 0), (1, 0, 0), (0, 1, 1), (0, 0, 1), (1, 1, 1)

             -1,0,-1    1,0,-1      2,0,-1,   2,3,3      2,3,4       5,5,5

             0,-1       0,1        0,2         0,2
             1,0        1,0        1,0         1,3
             2,-1       2,-1       2,-1        2,3
             1,0        1,0        3,0         3,0

             (0, 1, 0), (1, 0, 0), (0, 0, 0), (1, 0, 1), (0, 0, 1), (1, 1, 0)

             0,-1       0,1        0,1         0,3       0,3         0,5
             1,0        1,0        1,0         1,0       1,0         1,5
             2,-1       2,-1       2,-1        2,3       2,4         2,4
"""
import copy
import sys

# solution 1
def find_block_solution1(blocks):
    for search_range in range(1,len(blocks),2):
        idx = search_block(blocks, search_range)
        if idx >= 0:
            return idx + int(search_range / 2), int(search_range / 2), blocks[idx:idx+search_range]
        elif idx == -2:
            return -1, -1,[]


def search_block(blocks, search_range):
    size = len(blocks) - 1 if search_range >= len(blocks) else search_range
    for i in range(len(blocks) - size + 1):
        if check_block(blocks[i:i+size]):
            return i
    return -2 if size == len(blocks) - 1 else -1


def check_block(blocks):
    res = [False for _ in range(len(blocks[0]))]
    for i in range(len(blocks[0])):
        for j in range(len(blocks)):
            res[i] = res[i] or blocks[j][i]
    return all(res)


input_blocks = [
{"gym":False, "grocery_store":True, "office":False},
{"gym":False, "grocery_store":False, "office":False},
{"gym":True, "grocery_store":False, "office":True},
{"gym":True, "grocery_store":False, "office":True},
{"gym":False, "grocery_store":False, "office":True},
{"gym":True, "grocery_store":False, "office":False}
]

# solution 1
input_blocks = [
[False, True, False],
[False, False, False],
[False, False, False],
[False, False, False],
[False, False, False],
[True, False, True],
[False, False, True],
[True, False, False],
[True, False, False],
[False, True, False]
]

idx, n, res = find_block_solution1(input_blocks)
print(f"solution1 -- min_dist: {n},  idx:{idx}, res: {res}")