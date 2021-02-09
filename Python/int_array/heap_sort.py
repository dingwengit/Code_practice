"""
           5
         /    \
        -4    -3
        / \   / \
       8  20 2  11
"""
# binary tree can be represented as array as below
# a = [5, -4, -3, 8, 20, 2, 11]


# this function will put the max value into the root
def heapify(a, root, l):
    if root < 0:
        return

    left = root * 2 + 1
    right = root * 2 + 2

    if left < l and a[left] > a[root]:
        a[left], a[root] = a[root], a[left]
    if right < l and a[right] > a[root]:
        a[right], a[root] = a[root], a[right]

    heapify(a, root - 1, l)


def heap_sort(a):
    for i in range(len(a)):
        heapify(a, (len(a) - i) / 2, len(a) - i)
        a[0], a[len(a) - i - 1] = a[len(a) - i - 1], a[0]


a = [5, -4, -3, 8, 20, 2, 11]
heap_sort(a)
print a
