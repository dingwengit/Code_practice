# for mapping of int to letter
# 1 --> A
# 2 --> B
# 3 --> C ...
# 26 --> Z
# for a given digit array, find out how many ways you can decode it into
# different strings

# input = "22450"
# invalid input: 0000, 11150, 0123
# output: 2, 2, 4, 5 or 22, 4, 5 or 2, 24, 5

cnt = 0


def find_decode_cnt(s, idx):
    global cnt
    if idx >= len(s):
        cnt += 1
        return
    if int(s[idx]) > 0: # validation
        find_decode_cnt(s, idx+1)
    else:
        return
    if idx+2 <= len(s) and int(s[idx:idx+2]) <= 26 and int(s[idx:idx+2]) > 0: # validation
        find_decode_cnt(s, idx + 2)


s = "20225"
find_decode_cnt(s, 0)
print(cnt)

