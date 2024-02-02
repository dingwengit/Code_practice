#!/usr/bin/env python
from array import *

# give NxN square board, each row can place one queen, find out all possible
#  placements of placing queens in all rows without attacking each other

#  x o x x x
#  x x x o x
#  o x x x x
#  x x o x x

#  x o x x
#  x x x o
#  o x x x
#  x x o x

#  x x o x
#  o x x x
#  x x x o
#  x o x x


cnt = 0


def validate_pos(board, n, row, col):
    if any(board[row]):
        return False
    for r in range(row):
        if board[r][col]:
            return False
    for i in range(1, n):
        if row - i >=0 and col - i >=0 and board[row - i][col - i]:
            return False
        if row - i >=0 and col + i < n and board[row - i][col + i]:
            return False
    return True


def find_diff_placement(board, n, row=0):
    global cnt
    if row >= n:
        cnt += 1
        return

    # place board in row idx
    for col in range(n):
        if validate_pos(board, n, row, col):
            board[row][col] = True
            find_diff_placement(board, n, row+1)
            board[row][col] = False

n = 4
board = [[False for i in range(n)] for j in range(n)]
find_diff_placement(board, n)
print(f"placement: {cnt}")
