# for a NxN maze, find out how many different ways to start from (0,
# 0) to exit (N-1, N-1) -- one can only go right or down?


def get_ways_exit_maze(x, y):
    if x < 0 or y < 0:
        return 0

    if x == 0 and y == 0:
        return 1

    # print(f"x={x}, y={y}")

    return get_ways_exit_maze(x - 1, y) + get_ways_exit_maze(x, y - 1)


# n x n
def maze_traverse(n, i, j):
    if i >= n or j >= n:
        return 0

    if i == n - 1 and j == n - 1:
        return 1

    return maze_traverse(n, i + 1, j) + maze_traverse(n, i, j + 1)


n = 2
print(maze_traverse(n, 0, 0))
print(get_ways_exit_maze(n - 1, n - 1))