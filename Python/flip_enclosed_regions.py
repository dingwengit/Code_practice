# | 0  0  0  0 |
# | 1  0  1  0 |
# | 0  1  1  0 |
# | 0  0  0  0 |
# output:
# | 0  0  0  0 |
# | 1  0  0  0 |
# | 0  0  0  0 |
# | 0  0  0  0 |

# convert all '1's into '0's that cannot reach the boundary of the matrix
# assume matrix is square
from array import *


def check_neighbors(a, i, j, queue):
    if i-1>=0 and a[i-1][j] == 1:
        queue.append((i-1, j))
    if i+1 < len(a[0]) and a[i+1][j] == 1:
        queue.append((i+1, j))
    if j+1 < len(a[0]) and a[i][j+1] == 1:
        queue.append((i, j+1))
    if j-1 >= 0 and a[i][j-1] == 1:
        queue.append((i, j-1))


# a is list of list
def convert_ones(a):
    queue = []
    n = len(a[0])
    for i in range(n):
        for j in range(n):
            if (i == 0 or j == 0 or i == n-1 or j == n-1) and a[i][j] == 1:
                queue.append((i, j))

    while( len(queue) > 0 ):
        i, j = queue.pop(0)
        if a[i][j] == -1:
            continue
        a[i][j] = -1
        check_neighbors(a, i, j, queue)

    for i in range(n):
        for j in range(n):
            if a[i][j] == -1:
                a[i][j] = 1
            elif a[i][j] == 1:
                a[i][j] = 0
n = 4
# this does not work -- a = [[0] * n] * n
a = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
a[1][0] = 1
a[1][2] = 1
a[2][2] = 1
#a[2][1] = 1
a[3][1] = 1

for r in a:
    print r
convert_ones(a)
print "============="
for r in a:
    print r
