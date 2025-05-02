'''
Question You have a line of two dimensional pillars of different integral
heights. As rain falls in seattle, water accumulates in between the
pillars. Take an array of numbers as pillar heights. Calculate the area for
the amount of water that can get accumulated between pillars.
 example 1

                       |
    |  x  x   x  x  x  |
    |  x  x   |  x  x  |  |
    |  |  x   |  x  x  |  |
 |  |  |  |   |  x  |  |  |  |
 |  |  |  |   |  |  |  |  |  |
==========================
[2, 5, 3, 2,  4, 1, 2, 6, 4, 2]
[(2,1)]
   [(5,1)]
    [(5,1),(3,1)]
      [(5,1),(3,1),(2,1)]
             [(5,1),(4,3)] a=3
               [(5,1),(4,3), (1,1)] a=3
                  [(5,1),(4,3),(2,2)] a=4
                    [(6,1)] a=4 + 3 + 2 x 3 = 13
[(element height, count)]
*** the first element must be the highest level
'''

def water_amount_solution1(a):
    if len(a) <= 1:
        return 0
    area, res = 0, [(a[0], 1)]
    for idx in range(1, len(a)):
        h = a[idx]
        new_h, new_cnt = min(h, res[0][0]), 1
        res_idx = len(res) - 1
        while(res_idx >= 0):
            cur_h, cnt = res[res_idx]
            # print(f"h={h}, cur_h={cur_h}")
            if h < cur_h:
                res.append((h, new_cnt))
                break
            elif h == cur_h:
                res[res_idx] = cur_h, cnt+new_cnt
                break
            elif res_idx > 0:
                area += (new_h - cur_h) * cnt
                new_cnt += cnt
                res.pop()
            res_idx -= 1
        if res[0][0] <= h:
            res[0] = (h, 1)
        print(f"{res}, area={area}")
    return area

a=[2, 5, 3, 2, 4, 1, 2, 6, 4, 2]
a = [9,8,9,10,2,5,3,3,5,1,2,6,4]
area = water_amount_solution1(a)
print(f"solution1: {area}")

'''
Solution 2
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
