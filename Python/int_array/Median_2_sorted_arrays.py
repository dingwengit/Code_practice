# given two sorted arrays: a1=[2, 6, 8, 10, 12], a2=[3, 5, 7, 9, 11],
# find the median of two arrays
#  [1,  2, 3, 4, 5]
#   i1            j1 --> m1 = (i1 + j1) / 2 (inclusive)
#  [6, 7, 8, 9, 10]
#   i2            j2 --> m2 = (i2 + j2) / 2 (inclusive)
# if a[m1] > b[m2] --> first half of a, second half of b
# base case:
# [1,2]
# [3,4]
# median --> (2+3) / 2
#  let's assume both array is the same length
#

def get_median2(a, i1, j1, b, i2, j2):
    if i1 == j1 and i2 == j2:
        return (a[i1] + b[i2]) /2
    if i1 + 1 == j1 and i2 + 1 == j2:
        return (max(a[i1], b[i2]) + min(a[j1], b[j2])) / 2

    m1 = (i1 + j1) // 2
    m2 = (i2 + j2) // 2
    if a[m1] < b[m2]:
        return get_median2(a, m1, j1, b, i2, m2)
    else:
        return get_median2(a, i1, m1, b, m2, j2)


a1 = [1, 3, 5, 7, 9]
a2 = [2, 4, 6, 8, 10]

print(get_median2(a1, 0, len(a1)-1, a2, 0, len(a2)-1))
