# given street blocks with some attributes, find a block which has shortest
# distance of given set of attributes are True
# for example:
"""
input_blocks = [
{"gym":False, "grocery_store":True, "office":False}, # res [(F,0), (T,0),(F,0)] (T/F, index)
{"gym":False, "grocery_store":True, "office":False}, # res [(F,0), (T,1),(F,0)]
{"gym":False, "grocery_store":False, "office":False}, # res [(F,0), (T,1),(F,0)]
{"gym":True, "grocery_store":False, "office":True},   # res [(T,3), (T,1),(T,3)] -> dist = 2
{"gym":True, "grocery_store":False, "office":True},   # res [(T,4), (T,1),(T,4)]
{"gym":False, "grocery_store":True, "office":True},   # res [(T,4), (T,5),(T,5)] -> dis = 1
{"gym":True, "grocery_store":False, "office":False}    # res [(T,6), (T,5),(T,5)]
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