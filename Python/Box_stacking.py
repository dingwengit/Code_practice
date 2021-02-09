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
    for (l, w, h) in boxes:
        l1, w1, h1 = res[len(res) - 1]
        area = l1 * w1
        if l * w < area:
            res.append((l, w, h))
            print("** area = {}, {}".format(area, res))
            find_max_height(boxes, res)
            del res[len(res) - 1]


b1 = box(1, 2, 3)
b2 = box(1, 2, 3)
boxes = b1.r_boxes + b2.r_boxes
for (l, w, h) in boxes:
    res = []
    res.append((l, w, h))
    find_max_height(boxes, res)
    print(res)
