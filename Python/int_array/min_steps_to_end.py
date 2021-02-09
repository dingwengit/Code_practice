# given an array of steps [2,3,1,1,2,4,2,0,1,1], each integar "i" means that
# you can jump from 1 step to i steps.
# write a function to find out the min steps to reach to the end (from the
# start)
# here end means the last position of array
#           [2,3,1,1,2,4,2,0,1,1]
# cursteps [ 0, 10,  10, 10,  10, 10,  10, 10,  10, 10]
# idx -> 2 [ 0, 1, 1, 10,  10, 10,  10, 10,  10, 10]
import sys


def jump(a, idx, cur_steps, steps):
    global min_steps
    for i in range(a[idx], 0, -1):
        if idx + i >= len(a):
            continue
        steps[i + idx] = min(cur_steps + 1, steps[i + idx])
        if  i + idx == len(a) - 1:
            min_steps = min(min_steps, steps[i + idx])
            return
        jump(a, idx+i, steps[idx+i], steps)

a = [2,3,1,1,2,4,2,0,1,1]
min_steps = len(a)
steps = [len(a)] * len(a)
jump(a, 0, 0, steps)
print ("min_steps = {}".format(min_steps))
