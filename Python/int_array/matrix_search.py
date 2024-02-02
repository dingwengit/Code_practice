# given a 2D matrix, with sorted row and sorted columns, find a given integer
#
#
#
a = [
    [2, 4, 6, 8],
    [10, 12, 14, 16],
    [19, 20, 22, 24],
    [26, 28, 30, 32]
]


def find_number_in_row(arr, val, st, end):
    if st > end or st < 0:
        return False

    mid = (st + end) // 2
    if arr[mid] == val:
        return True
    elif arr[mid] < val:
        return find_number_in_row(arr, val, mid + 1, end)
    else:
        return find_number_in_row(arr, val, st, mid - 1)
    return False


def find_number(a, val, row_st, row_end):
    if row_st > row_end or row_st < 0 or row_st >= len(a):
        return False
    # 1 check mid row -- last element --> first element --> current row
    row_mid = (row_st + row_end) // 2
    # check if the value on the end of the row
    col = len(a[row_mid]) - 1
    if a[row_mid][col] == val:
        return True
    elif a[row_mid][col] < val:
        find_number(a, val, row_mid + 1, row_end)

    if a[row_mid][0] == val:
        return True
    elif a[row_mid][0] > val:
        return find_number(a, val, row_st, row_mid - 1)
    else:
        return find_number_in_row(a[row_mid], val, 0, col)


print(find_number(a, 1, 0, len(a)))
