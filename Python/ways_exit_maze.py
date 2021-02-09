# for a NxN maze, find out how many different ways to start from (0,
# 0) to exit (N-1, N-1)

def get_ways_exit_maze(x, y):
    if x == 0 and y == 0:
        return 1

    if x - 1 >= 0:
        return 1 + get_ways_exit_maze(x-1, y)

    if y - 1 >= 0:
        return 1 + get_ways_exit_maze(x, y-1)


def get_ways_exit_maze2(x, y, n):
    if x == n and y == n:
        return 1
    if x + 1 <= n:
        return 1 + get_ways_exit_maze2(x+1, y, n)
    if y + 1 <= n:
        return 1 + get_ways_exit_maze2(x, y+1, n)
print(get_ways_exit_maze(3, 3))
print(get_ways_exit_maze2(0, 0, 3))

