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

# solution: start from each element of boundary, and mark as False in a set()
#
from array import *

visited = set()
boundary_connected = set()


def search_connection(a):
    n = len(a[0])
    for i in range(0, n):
        for j in [0, n-1]:
            dfs(a, i, j)
            dfs(a, j, i)


def dfs(a, i, j):
    if (i, j) in visited:
        return
    n = len(a[0])
    visited.add((i, j))
    if a[i][j] == 0:
        return
    boundary_connected.add((i,j))
    if i + 1 < n and (i+1, j) not in visited:
        dfs(a, i+1, j)
    if i - 1 >= 0 and (i-1, j) not in visited:
        dfs(a, i-1, j)
    if j + 1 < n and (i, j+1) not in visited:
        dfs(a, i, j+1)
    if j - 1 >= 0 and (i, j-1) not in visited:
        dfs(a, i, j-1)


def print_result(a):
    n = len(a[0])
    for i in range(0, n):
        for j in range(0, n):
            if a[i][j] == 1 and (i, j) not in boundary_connected:
                a[i][j] = 0

    print(a)

# def check_neighbors(a, i, j, queue):
#     if i-1>=0 and a[i-1][j] == 1:
#         queue.append((i-1, j))
#     if i+1 < len(a[0]) and a[i+1][j] == 1:
#         queue.append((i+1, j))
#     if j+1 < len(a[0]) and a[i][j+1] == 1:
#         queue.append((i, j+1))
#     if j-1 >= 0 and a[i][j-1] == 1:
#         queue.append((i, j-1))
#
#
# # a is list of list
# def convert_ones(a):
#     queue = []
#     n = len(a[0])
#     for i in range(n):
#         for j in range(n):
#             if (i == 0 or j == 0 or i == n-1 or j == n-1) and a[i][j] == 1:
#                 queue.append((i, j))
#
#     while( len(queue) > 0 ):
#         i, j = queue.pop(0)
#         if a[i][j] == -1:
#             continue
#         a[i][j] = -1
#         check_neighbors(a, i, j, queue)
#
#     for i in range(n):
#         for j in range(n):
#             if a[i][j] == -1:
#                 a[i][j] = 1
#             elif a[i][j] == 1:
#                 a[i][j] = 0
# n = 4
# this does not work -- a = [[0] * n] * n
a = [[0, 0, 0, 0],
     [1, 0, 1, 0],
     [0, 1, 0, 0],
     [0, 0, 1, 0]]

search_connection(a)
print_result(a)
