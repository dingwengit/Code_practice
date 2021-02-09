# given two sorted arrays: a1=[2, 6, 8, 10, 12], a2=[3, 5, 7, 9, 11],
# find the median of two arrays
#  [2,  6, 8, 10, 12]
#   i1            j1 --> m1 = (i1 + j1) / 2 (inclusive)
#  [3, 5, 7, 9, 11]
#   i2            j2 --> m2 = (i2 + j2) / 2 (inclusive)
#  let's assume both array is the same length
#
def get_median(a1, i1, j1, a2, i2, j2):
    if i1 == j1 or i2 == j2:
        print "{} : {}".format(a1[i1], a2[i2])
        return (a1[i1] + a2[i2]) / 2

    if i1 + 1 == j1 or i2 + 1 == j2: # if 2 elements left, take the max of
        # left elements and min of the right elements, and divide by 2
        left = max(a1[i1], a2[i2])
        right = min(a1[j1], a2[j2])
        print "{} : {}".format(left, right)
        return (left + right)/2

    m1 = (i1 + j1) / 2
    m2 = (i2 + j2) / 2
    if a1[m1] > a2[m2]:
        return get_median(a1, i1, m1, a2, m2, j2)
    else:
        return get_median(a1, m1, j1, a2, i2, m2)

a1 = [1, 3, 5, 7, 9]
a2 = [4, 6, 8, 10, 11]

print get_median(a1, 0, len(a1)-1, a2, 0, len(a2)-1)
