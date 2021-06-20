#!/usr/bin/env python
from array import *

# give NxN square board, each row can place one queen, find out all possible
#  placements of placing queens in all rows without attacking each other


def check_placement(n, rows, row_idx, col):
    if row_idx == 0:
        return True
    for i in range(row_idx): # check all rows before row_idx
        r1, c1, r2, c2 = i, rows[i], row_idx, col
        if c2 == c1 or abs(c2-c1) == abs(r2-r1):
            return False
    return True


def place_queens(n, rows, row_idx):
    if row_idx >= n:
        for i in range(len(rows)):
            row = ["x"] * n
            row[rows[i]] = "O"
            print(' '.join(row))
            # print ("({}, {})".format(i+1, rows[i]+1))
        print("=====")
        return

    for i in range(n):
        # check if we can place a queen in row_idx, col = i
        rows[row_idx] = i
        if check_placement(n, rows, row_idx, i):
            place_queens(n, rows, row_idx + 1)

if __name__ == '__main__':
    n = 5
    rows = [0] * n # !!!! array index is row_idx where its value is column,
    # so we don't need back-tracking
    place_queens(n, rows, 0)