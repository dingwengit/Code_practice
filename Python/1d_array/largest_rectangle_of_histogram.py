'''
Find the largest rectangular area possible in a given histogram where
the largest rectangle can be made of a number of contiguous bars.
For simplicity, assume that all bars have same width and the width is 1 unit.
For example, consider the following histogram with 7 bars of heights

|                   |
|       |     |     |
|       |  |  |     |
|       |  |  |  |  |
|   |   |  |  |  |  |
|   |   |  |  |  |  |
{6, 2,  5, 4, 5, 3, 6}. The largest possible rectangle possible is 15
       {6,     2,       5,       4,         5,        3,           6}.
area    6      6        6        8          12        12           15
common (6,1) (2, 2)  (2, 3)   (2, 4)    (2, 5)     (2, 6)      (2, 7)
                     (5, 1)   (4, 2)    (4, 3)     (3, 4)      (3, 5)
                                        (5, 1)                 (6, 1)
common -- (height, cnt)
'''

def get_rect_histogram(a, res):
    max_area = 0
    for i in a:
        new_h, new_c = i, 1
        idx = len(res)-1
        add_c = 0
        while(idx >= 0):
            h, c = res[idx]
            if new_h <= h:
                add_c = c
                res.pop()
            else:
                res[idx] = h, c+1
                max_area = max(max_area, h * (c+1))
            idx -= 1
        new_c += add_c
        max_area = max(max_area, new_h * new_c)
        res.append((new_h, new_c))
        print(f"i={i}, res={res}")
    return max_area

print(get_rect_histogram([6, 2, 5, 4, 5, 3, 6], []))

