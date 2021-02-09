# given an int array, e.g., 3, 5, 17, 4, 8, 12, 9, 10, find the longest
# increasing sequence (3, 4, 8, 9, 10)

#  a =     3,  5,   17,   4,  8, 12, 9, 10
#  length  1   2    3     2
# assumption: unique integers
# Question: do we need to return the count or the actual int sequence array?
# there could be multiple squence arrays (having the same result)
# option 1 is to use another array to store the count per integer
# option 2 is to use hash table to store the max count
# c = {3:[3], 5:[3,5], 17:[3,5,17], 4:2, 8:3, 12:4, 9:4, 10:5}

import copy

def increasing_seq(a):
    r = []
    h = {}
    len_seq = 0
    for i in a:
        max_len = 0
        res = []
        for k in h.keys():
            if i > k and max_len < len(h[k]):
                max_len = len(h[k])
                res = copy.copy(h[k])
        res.append(i)
        h[i] = res
        # print h
        if len_seq < len(res):
            len_seq = len(res)
            r = res
    print(r)

def find_nondecreasing_max_seq(a):
    length_arr = [1] * len(a)
    for i in range(1, len(a)): # start with index 1
        length_arr[i] = 1 + max(length_arr[j] if a[i] >= a[j] else 0 for j \
                in range(i))
    return max(length_arr)


a = [3, 5, 17, 4, 8, 12, 9, 10]
s = "abc"
y = [c for c in s if c < 'c']
x = next((i+1 for i, v in enumerate(a) if v == 15), -1)
print("y:{}".format(y))
print("x:{}".format(x))
for i, v in enumerate(a):
    print("i:{}, a:{}".format(i, v))

# increasing_seq(a)
# print(find_nondecreasing_max_seq(a))
