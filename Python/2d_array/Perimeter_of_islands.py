'''
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).


The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island.
Also, row == grid.length and col == grid[i].length

Determine the perimeter of the island.

Example 1:
Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.

Example 2:

Input: grid = [[1]]
Output: 4

Example 3:

Input: grid = [[1,0]]
Output: 4

'''


a = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]

def find_perimeter_rec(a, r, c, visited):
    k1 = format(f"{r}-{c}")
    # move down
    if r+1 < len(a) and a[r+1][c] == 1:
        k2 = format(f"{r + 1}-{c}")
        if k2 in visited:
            if 't' in visited[k2]:
                visited[k2].remove('t')
        else:
            visited[k2] = {'l','r','b'}
            find_perimeter_rec(a, r+1, c, visited)
        if 'b' in visited[k1]:
            visited[k1].remove('b')

    # move right
    if c+1 < len(a[0]) and a[r][c+1] == 1:
        k2 = format(f"{r}-{c+1}")
        if k2 in visited:
            if 'l' in visited[k2]:
                visited[k2].remove('l')
        else:
            visited[k2] = {'t','r','b'}
            find_perimeter_rec(a, r, c+1, visited)
        if 'r' in visited[k1]:
            visited[k1].remove('r')

    # move left
    if c-1 >= 0 and a[r][c-1] == 1 :
        k2 = format(f"{r}-{c-1}")
        if k2 in visited:
            if 'r' in visited[k2]:
                visited[k2].remove('r')
        else:
            visited[k2] = {'t','l','b'};
            find_perimeter_rec(a, r, c-1, visited)
        if 'l' in visited[k1]:
            visited[k1].remove('l')

    # move up
    if r-1 >= 0 and a[r-1][c] == 1 :
        k2 = format(f"{r-1}-{c}")
        if k2 in visited:
            if 'b' in visited[k2]:
                visited[k2].remove('b')
        else:
            visited[k2] = {'t','l','t'}
            find_perimeter_rec(a, r-1, c, visited)
        if 't' in visited[k1]:
            visited[k1].remove('t')


def find_perimeter(a):
    perimeter, visited = 0, dict()
    for r in range(len(a)):
        for c in range(len(a[0])):
            if a[r][c] == 1:
                visited[format(f"{r}-{c}")] = {'l','r','b','t'}
                find_perimeter_rec(a, r, c, visited)
                break;

    for v in visited.values():
        perimeter += len(v)
    return perimeter

print(find_perimeter(a))
