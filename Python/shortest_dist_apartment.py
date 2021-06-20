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
block_idx: 0 -- 1 -- 2 -- 3 -- 4 -- 5
search_range = min(len(blocks)-1, cur_min_distance)
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
    sr = min(len(blocks)-1, cur_min)
    att_tbl = copy.deepcopy(blocks[idx])
    for s_idx in range(sr+1):
        if check_attributes(blocks, s_idx, idx, att_tbl):
            return True, s_idx
    return False, sr

def find_shortest_blocks(blocks):
    min_dist = sys.maxsize
    min_idx = sys.maxsize
    for idx in range(len(blocks)):
        found, dist= find_shortest_block(blocks, idx, len(blocks)-1)
        if found and dist < min_dist:
            min_dist = dist
            min_idx = idx
    return min_dist, min_idx

input_blocks = [
{"gym":False, "grocery_store":True, "office":False},
{"gym":False, "grocery_store":True, "office":False},
{"gym":True, "grocery_store":False, "office":False},
{"gym":True, "grocery_store":False, "office":True},
{"gym":False, "grocery_store":False, "office":True},
{"gym":True, "grocery_store":False, "office":False}
]
dist, idx = find_shortest_blocks(input_blocks)
print(f"min_dist: {dist}, idx:{idx} - {input_blocks[idx]}" )