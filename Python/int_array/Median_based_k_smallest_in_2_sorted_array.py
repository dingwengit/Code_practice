# arr1 = [3, 4, 5, 6, 7, 8, 9]
# arr2 = [1, 2]
# k = 5
# return: 5
import sys

def get_val(a, i):
    if i >= len(a):
        return sys.maxsize
    else:
        return a[i]


def get_medium(arr1, s1, e1, arr2, s2, e2, k):
#    print ("s1:{}, e1:{}, s2:{}, e2:{}".format(s1, e1, s2, e2))
    if e1 - s1 <= 1 and e2 - s2 <= 1:
        a1 = max(get_val(arr1, s1), get_val(arr2, s2))
        a2 = min(get_val(arr1, e1), get_val(arr2, e2))
#        print("a1:{}".format(a1))
#        print("a2:{}".format(a2))
        return min(a1, a2) if s1 + s2 + 2 >= k else max(a1, a2)

    m1 = s1 + (e1 - s1) // 2
    m2 = s2 + (e2 - s2) // 2
    if get_val(arr1, m1) > get_val(arr2, m2):
        return get_medium(arr1, s1, m1, arr2, m2, e2, k)
    else:
        return get_medium(arr1, m1, e1, arr2, s2, m2, k)

arr1 = [2, 4, 5, 6, 7, 18, 19]
arr2 = [1, 15]
k = 2
# !!!! === the point is that using k-1 as end position
print(get_medium(arr1, 0, k - 1, arr2, 0, k - 1, k))
