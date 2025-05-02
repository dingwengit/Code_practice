"""
           5
         /    \
        -4    -3  <-- start from this level
        / \   / \
       8  20 2  11

            20
         /     \
        5      11
        / \    /  \
       -4  8  -3   2
                    \
                    30
      layer = 2
       (8, 3) -> (-4, 3) -> (11, 2) -> (5, 2) -> (20,1)

      contour = [20, 5, -4, 30]
"""
# binary tree can be represented as array as below
# a = [5, -4, -3, 8, 20, 2, 11]
#            1   2   3  4  5   6   7  8  9
# heap_a = [20, 5, 11, -4, 8, -3, 2, -5, 30]
# p_idx = c_idx / 2

# this function will put the max value into the root
def heapify(a, root, l):
    if root < 0:
        return

    left = root * 2 + 1
    right = root * 2 + 2

    print(f"l={left}, r={right}, r_idx={root}")

    if left < l and a[left] > a[root]:
        a[left], a[root] = a[root], a[left]
    if right < l and a[right] > a[root]:
        a[right], a[root] = a[root], a[right]

    heapify(a, root - 1, l)


def heap_sort(a):
    # a[0] will be the biggest int after each iteration of heapifying the array
    for i in range(len(a)):
        heapify(a, int((len(a) - i) / 2), len(a) - i)
        a[0], a[len(a) - i - 1] = a[len(a) - i - 1], a[0]


 # a = [5, -4, -3, 8, 20, 2, 11, 7, 9, 3, 12]
a = [1,2,3,4,5]

"""
           5
         /    \
        1      3
        / \   
       2   4 
"""
heap_sort(a)
print(a)
