# for mapping of int to letter
# 1 --> A
# 2 --> B
# 3 --> C ...
# 26 --> Z
# for a given digit array, find out how many ways you can decode it into
# different strings

cnt = 0

map = {}

def set_map(map):
    for i in range(0, 26):
       map[i + 1] = chr(ord('A') + i)

def decode(str, pos, map):
    global cnt
    print "pos: {}, cnt:{}".format(pos, cnt)
    if pos >= len(str):
        return
    if int(str[pos]) in map:
        if pos == len(str) - 1 :
            cnt += 1
        decode(str, pos + 1, map)
    if pos + 1 < len(str) and int(str[pos:pos+2]) in map:
        if pos + 1 == len(str) - 1 :
            cnt += 1
        decode(str, pos + 2, map)

str = "162"
set_map(map)
print map
decode(str, 0, map)
print cnt
