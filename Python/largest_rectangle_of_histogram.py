# Find the largest rectangular area possible in a given histogram where
# the largest rectangle can be made of a number of contiguous bars.
# For simplicity, assume that all bars have same width and the width is 1 unit.
#For example, consider the following histogram with 7 bars of heights
# {6, 2, 5, 4, 5, 1, 6}. The largest possible rectangle possible is 12
#        {6,     2,       5,       4,         5,        3,           6}.
# area    6      6        6        8          12        12           12
# common (6,1) (2, 2)  (2, 3)   (2, 4)    (2, 5)     (2, 6)      (2, 7)
#                      (5, 1)   (4, 2)    (4, 3)     (3, 4)      (3, 5)
#                                         (5, 1)
# common -- (height, cnt)


def get_rect_histogram(a, res):
    max_area = 0
    for i in a:
        found_bigger, purge = False, False
        for j in range(len(res)):
            if purge:
                res.pop()
                continue
            (h, c) = res[j]
            if h >= i:
                res[j] = (i, c+1)
                max_area = max(max_area, i * (c+1))
                found_bigger = True
                if h > i:
                    purge = True
            else:
                found_bigger = False
                res[j] = (h, c+1)
                max_area = max(max_area, h * (c + 1))

        if len(res) == 0 or not found_bigger:
            res.append((i, 1))
            max_area = max(max_area, i)
        print(f"i={i}, res={res}")
    return max_area

print(get_rect_histogram([6, 2, 5, 4, 5, 3, 6], []))

