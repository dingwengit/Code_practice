# given two sorted arrays: a1=[2, 6, 8, 10, 12], a2=[3, 5, 7, 9, 11],
# find the median of two arrays
#  [1,  2, 3, 4, 5]
#   i1            j1 --> m1 = (i1 + j1) / 2 (inclusive)
#  [6, 7, 8, 9, 10]
#   i2            j2 --> m2 = (i2 + j2) / 2 (inclusive)
# because median is the element that is > (m + n) // 2 elements for the combined sorted array
# so method is to merging 2 sorted arrays and when count == (m + n) //2, return that element

def get_median(a, b):
    m, n= len(a), len(b)
    m_idx = (m+n)//2
    i, j, cnt = 0, 0, 0

    while (i < m and j < n):
        if a[i] < b[j]:
            if cnt == m_idx:
                return a[i]
            i += 1
        else:
            if cnt == m_idx:
                return b[j]
            j += 1
        cnt += 1

    while (i < m):
        if cnt == m_idx:
            return a[i]
        i += 1
        cnt += 1

    while (j < n):
        if cnt == m_idx:
            return b[j]
        j += 1
        cnt += 1
    return None

a1 = [1, 3]
a2 = [2, 4, 6, 8, 10]


print(get_median(a1,a2))
