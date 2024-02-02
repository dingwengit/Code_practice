# given an array of steps [2,3,1,1,2,4,2,0,1,1], each integar "i" means that
# you can jump from 1 step to i steps.
# write a function to find out the min steps to reach to the end (from the
# start)
# here end means the last position of array
#           [2,3,1,1,2,4,2,0,1,1]
# cursteps [ 0,1,1,]
# idx -> 2 [ 0, 1, 1, 10,  10, 10,  10, 10,  10, 10]

def get_min_jumps(a):
    res = [0] * len(a)
    for idx, steps in enumerate(a):
        for j in range(1, steps+1):
            cur_step = res[idx] + 1
            if idx + j < len(a) and (cur_step < res[idx + j] or res[idx+j] == 0):
                res[idx + j] = cur_step
    return res[len(a) - 1]

def jump(a, idx, cur_steps, steps):
    global min_steps
    if idx == len(a) - 1:
        min_steps = min(min_steps, steps[idx])
        return
    for i in range(a[idx], 0, -1):
        if idx + i >= len(a):
            continue
        steps[i + idx] = min(cur_steps + 1, steps[i + idx])
        jump(a, idx+i, steps[idx+i], steps)

a = [2,3,1,1,2,4,2,0,1,1]
min_steps = len(a)
steps = [len(a)] * len(a) # initialize to the max steps
jump(a, 0, 0, steps)
print ("min_steps = {}".format(min_steps))
print ("min_steps = {}".format(get_min_jumps(a)))
