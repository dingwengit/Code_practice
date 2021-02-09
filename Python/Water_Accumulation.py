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


# check negative input

def water_accumalation(a):
    amt = 0
    res = [] # (height, cnt)
    for h in a:
        print res
        if len(res) > 0:
            (l_h, l_cnt) = res[len(res)-1]
            if h >= l_h:
                (f_h, f_cnt) = res[0]
                level = min(f_h, h)
                for idx in range(len(res)-1, -1, -1):
                    (idx_h, idx_cnt) = res[idx]
                    if idx_h >= level:
                        break
                    amt += (level - idx_h) * idx_cnt
                    res[idx] = (level, idx_cnt)
                if h >= res[0][0]:
                    res = []
        if len(res) == 0:
            res.append((h, 1))
        else:
            found = False
            new_cnt = 1
            for idx in range(len(res) - 1, -1, -1):
                (idx_h, idx_cnt) = res[idx]
                if h == idx_h:
                    found = True
                    new_cnt += idx_cnt
                    if idx < len(res) - 1:
                        del res[len(res) - 1]
                    res[idx] = (idx_h, new_cnt)
            if not found:
                res.append((h,1))
    return amt

a = [8,8,2,5,3,3,5,1,2,6,4]
print water_accumalation(a)
