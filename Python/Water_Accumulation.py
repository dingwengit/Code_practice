###Question You have a line of two dimensional pillars of different integral
# heights. As rain falls in seattle, water accumulates in between the
# pillars. Take an array of numbers as pillar heights. Calculate the area for
# the amount of water that can get accumulated between pillars.
#  example 1
#                 _
#     _     _    | |
#    | |   | |   | |_
#    | |_ _| |   | | |
#   _| | | | |  _| | |
#  | | | | | |_| | | |
#  | | | | | | | | | |
#==========================
#  [2,   5,    3,   3,      5,         1,    2,        6,         4]
# (0,2) (2,5) (5,3) (5, 3) (5, 5, 2)  (5,1) (5, 2, 1) (6, 6, 2)  (6, 4)
#                   (5, 3) (5, 5, 2)        (5, 2)    (6, 6, 2)
# *** the first element must be the highest level

#  example 2
#  _
# | |
# | |                __
# | |   _      __   | |
# | |  | |    | |   | |__
# | |  | |____| |   | | |
# | |__| | | | |   _| | |
# | |  | | | | |__| | | |
# | |  | | | | |  | | | |
#==========================
# 8 --> [8]
# 2 --> [8,2]
# 5 --> [8,5,5] -> 3
# 3 --> [8,5,5,3]
# 3 --> [8,5,5,3,3]
# 5 --> [8,5,5,5,5,5] --> 4
# 1 --> [8,5,5,5,5,5,1]
# 2 --> [8,5,5,5,5,5,2,2] --> 1
# 6 --> [8,6,6,6,6,6,6,6,6] --> 1+1+1+1+1+4+4 = 13
# 4 --> [8,6,6,6,6,6,6,6,6,4]

'''
Solution
1. for i in range(len(res))
1. if cur_h >= res[i] --> calculate the water amount and replace res[i] with
2. break
'''


def get_amount(h, res):
    amt = 0
    if h > res[0][0]:
        new_h = res[0][0]
        res[0] = (h, 1)
        return amt
    else:
        new_h = h

    found_idx = -1
    new_cnt = 1 # note that this starts with 1
    for idx in range (len(res)):
        ht, cnt = res[idx]
        if new_h >= ht:
            amt += (new_h - ht) * cnt
            new_cnt += cnt
            if found_idx == -1:
                found_idx = idx
    if found_idx == -1:
        res.append((new_h, 1))
    else:
        res[found_idx] = (new_h, new_cnt)
        for _ in range(found_idx+1, len(res)):
            res.pop()
    return amt


def water_accumalation(a):
    amt = 0
    if len(a) <= 1:
        return amt
    res = [(a[0], 1)] # (height, cnt)
    for idx in range(1, len(a)):
        h = a[idx]
        amt += get_amount(h, res)
        print(f"idx: {idx}, h:{h}, res: {res}")
    return amt


a = [9,8,9,10,2,5,3,3,5,1,2,6,4]
print(water_accumalation(a))
