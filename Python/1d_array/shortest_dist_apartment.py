# given street blocks with some attributes, find a block which has shortest
# distance of given set of attributes are True
# for example:
"""
input_blocks = [
{"gym":False, "grocery_store":True, "office":False}, # res [0,0,0] attributes [F,T,F]
{"gym":False, "grocery_store":True, "office":False}, # res [0,1,0] attributes [F,T,F]
{"gym":False, "grocery_store":False, "office":False}, # res [0,1,0] attributes [F,T,F]
{"gym":True, "grocery_store":False, "office":True},   # res [3,1,3] attributes [T,T,T]-> dist = 2
{"gym":True, "grocery_store":False, "office":True},   # res [4,1,4] attributes [T,T,T]
{"gym":False, "grocery_store":True, "office":True},   # res [4,5,5] attributes [T,T,T]-> dis = 1
{"gym":True, "grocery_store":False, "office":False}   # res [6,5,5] attributes [T,T,T]
]
"""
import sys

# linear solution
def find_block_solution(blks):
    res = [0] * len(blks[0]) # last index of that attribute = True
    attrbutes = [False] * len(blks[0])
    found, cnt = False, sys.maxsize
    for i, v in enumerate(blks):
        if all(v): # if all attributes are True in one block
            return True, 0
        if any(v) == False:
            continue
        for idx, attr in enumerate(v):
            if attr:
                res[idx] = i
                attrbutes[idx] = True
        if all(attrbutes):
            found = True
            pos_min, pos_max = sys.maxsize, 0
            for idx in res:
                pos_min = min(pos_min, idx)
                pos_max = max(pos_max, idx)
            # print(f"res={res}, pos_min={pos_min}, pos_max={pos_max}")
            cnt = min(cnt, pos_max - pos_min)

    return found, cnt


# solution
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

found, n = find_block_solution(input_blocks)
print(f"min_dist: {n},  found: {found}")