'''
There is a bot located at a pair of integer coordinates, (x, y). It must be moved to a location with another set of coordinates. Though the bot can move any number of times, it can only make the following two types of moves:
    From location (x, y) to location (x + y, y).
    From location (x, y) to location (x, x + y).
For example, if the bot starts at (1, 1), it might make the following sequence of moves:
(1, 1) → (1, 2) → (3, 2) → (5, 2). Note that movement will always be either up or to the right.
A grid with coordinates, showing a bot's possible moves from (1,1) to (5,2) via (1,2) and (3,2), moving up or right.

5
4
3
2  x1      x2      x3
1  x0
   1   2   3   4   5
Given starting and target ending coordinates, determine whether the bot can reach the ending coordinates given the rules of movement.
'''

def reach_point(res, n, x2, y2):
    x, y = res[len(res)-1]
    print(f"{x},{y}")
    if x == x2 and y == y2:
        return True

    if x + y <= x2:
        res.append((x+y, y))
        if reach_point(res, n, x2, y2):
            return True
        del res[len(res)-1]
    if x + y <= y2:
        res.append((x, x+y))
        if reach_point(res, n, x2, y2):
            return True

    return False

res = [(1,1)]
print(reach_point(res, 5, 3, 4))