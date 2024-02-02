"""
Longest Peak
Input array of integers, and returns the longest peak : peak as adjacent integers in the array that are strictly increasing until top and then strictly decreasing
Example:
[1,2,3,3,4,0,10,6,5,-1,-3,2,1]
# 6

[1,2,3,4,5,3,2,1,1,4,0,10,6,5,-1,-3,2,3]
# 8

    [1,2,3,3,4,0,10,6,5,-1,-3,2,1]
lR  [0,1,2,0,1,0, 1,0,0, 0, 0,1,0]
RL  [0,0,0,0,1,0, 4,3,2, 1, 0,1,0]
"""