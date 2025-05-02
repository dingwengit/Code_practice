# Given an m x n 2D binary grid which represents a map of'1's (land) and'0's (water),
# return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.
# | 1  1  0  0 |
# | 1  0  1  0 |
# | 0  1  1  0 |
# | 0  0  0  0 |

# 1,2 --> key = "1-2", "2-3"

a = [[0, 1, 0, 0],
     [1, 0, 1, 0],
     [1, 1, 0, 0],
     [1, 0, 1, 0]]

def find_number_islands(a):
    n = len(a[0])
    visited, cnt = set(), 0
    for i in range(n):
        for j in range(n):
            key = f"{i}-{j}"
            if key in visited:
                continue
            if a[i][j] == 1:
                cnt += 1
                visited.add(key)
                fillout_island(a, n, visited, i, j)
    return cnt


def fillout_island(a, n, visited, i, j):
    # go right
    x, y = i, j+1
    key = f"{x}-{y}"
    if y < n and a[x][y] == 1 and not key in visited:
        visited.add(key)
        fillout_island(a, n, visited, x, y)
    # go down
    x, y = i+1, j
    key = f"{x}-{y}"
    if x < n and a[x][y] == 1 and not key in visited:
        visited.add(key)
        fillout_island(a, n, visited, x, y)
    # go left
    x, y = i, j-1
    key = f"{x}-{y}"
    if y >= 0 and a[x][y] == 1 and not key in visited:
        visited.add(key)
        fillout_island(a, n, visited, x, y)
    # go up
    x, y = i-1, j
    key = f"{x}-{y}"
    if x >= 0 and a[x][y] == 1 and not key in visited:
        visited.add(key)
        fillout_island(a, n, visited, x, y)

print(find_number_islands(a))