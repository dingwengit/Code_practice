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
Solution:
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
             (0, 1, 0), (1, 0, 0), (1, 0, 0), (0, 1, 1), (0, 0, 1), (1, 0, 0)
"""
import copy
import sys


def check_attributes(blocks, s_idx, idx, att_tbl):
    if s_idx == 0 and all(att_tbl.values()):
         return True
    # check left block
    if idx - s_idx >=0:
        for key in blocks[idx - s_idx]:
            if blocks[idx - s_idx][key] and not att_tbl[key]:
                att_tbl[key] = True
                if all(att_tbl.values()):
                    return True
    # check right block
    if idx + s_idx < len(blocks):
        for key in blocks[idx + s_idx]:
            if blocks[idx + s_idx][key] and not att_tbl[key]:
                att_tbl[key] = True
                if all(att_tbl.values()):
                    return True
    return False


def find_shortest_block(blocks, idx, cur_min):
    att_tbl = copy.deepcopy(blocks[idx])
    for s_idx in range(cur_min+1):
        if check_attributes(blocks, s_idx, idx, att_tbl):
            return True, s_idx
    return False, cur_min


def find_shortest_blocks(blocks):
    min_dist = len(blocks)-1
    min_idx = sys.maxsize
    for idx in range(len(blocks)):
        found, dist= find_shortest_block(blocks, idx, min_dist)
        if found and dist < min_dist:
            min_dist = dist
            min_idx = idx
    return min_dist, min_idx

input_blocks = [
{"gym":False, "grocery_store":True, "office":False},
{"gym":False, "grocery_store":False, "office":False},
{"gym":True, "grocery_store":False, "office":True},
{"gym":True, "grocery_store":False, "office":True},
{"gym":False, "grocery_store":False, "office":True},
{"gym":True, "grocery_store":False, "office":False}
]
dist, idx = find_shortest_blocks(input_blocks)
print(f"min_dist: {dist}, idx:{idx} - {input_blocks[idx]}" )

# solution 2
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

#
# 1. copy new block into a var
# 2. loop through item in a
# 3. for item, if attr[i] in the new block is true, set item[i] to false
# 4. for item, if item[i] is true, set var[i] to true
# 5. if item has all attr as false, delete it from a
# 6. add the new block into a
# 7. if var has all attr as true, we found the solution,
# 8. delete the first item in a, and continue
#
def add_block(blocks, idx, a):
    block = copy.deepcopy(blocks[idx])
    removes = []
    for index, b in enumerate(a):
        for i, v in enumerate(block):
            if v and b[1][i]:
                b[1][i] = False
            if b[1][i]:
                block[i] = True
        if not any(b[1]):
            removes.append(index)
    for i in removes:
        del a[i]
    a.append((idx, blocks[idx]))
    if all(block):
        print(f"found solution -> a={a}")
        return a[len(a)-1][0] - a[0][0], int((a[len(a)-1][0] + a[0][0]) / 2)
    else:
        print(f"a={a}")
        return -1, -1


def find_best_block(blocks):
    a = []
    min_blocks = len(blocks)
    min_idx = 0
    for idx, b in enumerate(blocks):
        if all(b):
            return 1, idx
        n, found_idx = add_block(blocks, idx, a)
        if n != -1:
            if min_blocks > n:
                min_blocks = n
                min_idx = found_idx
            del a[0] # now remove the first candidate
    return min_blocks, min_idx


n, idx = find_best_block(input_blocks)
print(f"min_dist: {n} - idx:{idx} : {input_blocks[idx]}")
