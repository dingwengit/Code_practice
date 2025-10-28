'''
You are given row x col grid representing a map where
grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally).
The grid is completely surrounded by water,
and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside
isn't connected to the water around the island.
Also, row == grid.length and col == grid[i].length

Determine the perimeter of the island.

Example 1:
Input: grid = [
[0,1,0,0],
[1,1,1,0],
[0,1,0,0],
[1,1,0,0]
]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.

Solution:
cnt of empty surroundings or 0s c_z = [0] * 5
[0,1,0,0], --> for "1", there are only other "1" below, so c_z[3] += 1
[1,1,1,0], --> there are 2 "1"s, with only other "1" in its neighbor, so c_z[3] += 2
[0,1,0,0], --> for "1", there are other 2 "1"s in its neighbor, so c_z[2] += 1
[1,1,0,0]  --> for the first "1", there are other "1" in its neighbor, so c_z[3] += 1
               for the 2nd "1", there are 2 other "1"s in its neighbor, so c_z[2] += 1
So c_z = [0,0,2,4,0]
idx       0,1,2,3,4
output = 0 * 1 + 2 * 2 + 3 * 4 + 4 * 0 = 16

Example 2:

Input: grid = [[1]]
Output: 4

Example 3:

Input: grid = [[1,0]]
Output: 4

'''

a = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
