#!/usr/bin/env python

# Given unlimited boxes (l, w, h), each box can rotate
# write a function to return max height of tacking boxes that bottom area of
# the box must be decreasing

def find_max_height(boxes, res):
    global max_height
    l, w, h = res[len(res) -1]
    top_area = l * w
    for (l, w, h) in boxes:
        if l * w < top_area:
            res.append((l,w,h))
            max_height = max(max_height, sum(h for _,_,h in res))
            find_max_height(boxes, res)
            del res[len(res) - 1]


max_height = 0 # !!!! max height means the sum of height of all stacked boxes
l, w, h = (6, 3, 5)
boxes = [(6,3,5), (3,5,6), (6,5,3), (2,4,8), (8,4,2), (2,8,4)]
for (l, w, h) in boxes:
    res = [(l, w, h)]
    find_max_height(boxes, res)
print(max_height)
