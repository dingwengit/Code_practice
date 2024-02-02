# arr1 = [3, 4, 5, 6, 7, 8, 9]
# arr2 = [1, 2]
# connect them and find out the median
#
'''
 a = [(2,4),(6,8)], i = 0, j=len(a)=4
 max1 = 4, min1=6, p1=2
 b = [(1,3,5), (7,9)]
 max2 = 5, min2=7, p2=(4+5+1)//2 - p1 = 5 - 2 = 3
if max1 < min2 and max2 < min1:
    if len(a) + len(b) % 2 == 0:
        return (max(max1, max2) + min(min1, min2)) / 2
    else:
        return max(max1, max2)

a = (1,2), (3,4), i=0, j=4, p1=2
    max1=2, min1=3
b = (5,6,7), (8,9)
    max2=7, min2=8
    max2 > min1, so we need i = p1 + 1 = 3

a = (1,2,3),(4), i=3, j=4, p1 = 3
b = (5,6), (7,8,9), p2 = 5 - 3 = 2

a = (1,2,3,4), (MAX), i=4, j=4, p1 = 4
b = (5), (6,7,8,9), p2 = 5 - 4 = 1

'''

import sys

MIN = sys.maxsize * (-1)
MAX = sys.maxsize


def get_median_2_arrays(a, b):
    if len(a) > len(b):
        a, b = b, a
    print(f"a:{a}, b:{b}")
    low, high = 0, len(a)
    while( low <= high):
        p1 = (low + high) // 2
        p2 = (len(a) + len(b) + 1) // 2 - p1

        maxLeft1 = MIN if p1 == 0 else a[p1-1] # element up to position p1, because of 0 index, it is a[p1-1]
        minRight1 = MAX if p1 >= len(a) else a[p1]

        maxLeft2 = MIN if p2 == 0 else b[p2-1]
        minRight2 = MAX if p2 >= len(b) else b[p2]

        print(f"p1:{p1}, p2:{p2}, maxLeft1:{maxLeft1}, minRight1:{minRight1}, maxLeft2:{maxLeft2}, minRight2:{minRight2}, low:{low}, high:{high}")
        print(f"{a[:p1]}:{a[p1:]}")
        print(f"{b[:p2]}:{b[p2:]}")
        if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
            if (len(a) + len(b)) % 2 == 0:
                return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
            else:
                return max(maxLeft1, maxLeft2)
        elif maxLeft1 > minRight2:
            high = p1 -1
        else:
            low = p1 + 1


arr1 = [5, 6, 7, 8, 9]
arr2 = [1, 2, 3, 4]
# arr1 = [3, 4, 5, 6, 7, 8, 9]
# arr2 = [1, 2]
print(get_median_2_arrays(arr1, arr2))
