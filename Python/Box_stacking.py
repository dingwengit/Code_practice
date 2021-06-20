#!/usr/bin/env python

# Given unlimited boxes (l, w, h), each box can rotate
# write a function to return max height of tacking boxes that bottom area of
# the box must be decreasing

class box:
    def __init__(self, l, w, h):
        self.r_boxes = []
        # assume l != w != h
        self.r_boxes.append((l, w, h))
        self.r_boxes.append((l, h, w))
        self.r_boxes.append((h, w, l))


def find_max_height(boxes, res):
    global max_height
    for (l, w, h) in boxes:
        l1, w1, h1 = res[len(res) - 1]
        area = l1 * w1
        if l * w < area:
            res.append((l, w, h))
            max_height = max(max_height, sum(h for _,_,h in res))
            print("** area = {}, {}".format(area, res))
            find_max_height(boxes, res)
            del res[len(res) - 1]


max_height = 0 # !!!! max height means the sum of height of all stacked boxes
b1 = box(6, 3, 5)
boxes = b1.r_boxes
for (l, w, h) in boxes:
    res = [(l, w, h)]
    find_max_height(boxes, res)
print(max_height)
