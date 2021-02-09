# Find the largest rectangular area possible in a given histogram where
# the largest rectangle can be made of a number of contiguous bars.
# For simplicity, assume that all bars have same width and the width is 1 unit.
#For example, consider the following histogram with 7 bars of heights
# {6, 2, 5, 4, 5, 1, 6}. The largest possible rectangle possible is 12
#        {6,     2,       5,       4,         5,        1,           6}.
# area    6      6        6        8          12        12           12
# common (6,1) (2, 2)  (2, 3)   (2, 4)    (2, 5)     (1, 6)      (1, 7)
#                      (5, 1)   (4, 2)    (4, 3)                 (6, 1)
#                                         (5, 1)
# common -- (height, cnt)

max_area = 0


def get_rect_histogram(a, res):
    global max_area
    for i in a:
        found = False
        for j in range(len(res)):
            (h, c) = res[j]
            if h >= i:
                res[j] = (i, c+1)
                max_area = max(max_area, i * (c+1))
                if h == i:
                    found = True
            else:
                res[j] = (h, c+1)
                max_area = max(max_area, h * (c + 1))
        if len(res) == 0 or not found:
            res.append((i, 1))
            max_area = max(max_area, i)


get_rect_histogram([6, 2, 5, 4, 5, 1, 6], [])
print max_area
