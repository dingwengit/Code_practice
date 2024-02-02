"""
given int array [1 0 5 2 0 0 3], move all 0s to the right [1 5 2 3 0 0 0]
                   i         j
"""

# don't keep the order of non-zero digits
def move_zeros(a):
    i = 0
    j = len(a) - 1
    while(i < j):
        while a[i] != 0:
            i += 1
        while a[j] == 0:
            j -= 1
        if i < j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
    return a


# keep the order of non-zero digits
def move_zeros_order(a):
    i = 0
    while i < len(a):
        while  i < len(a) and a[i] != 0:
            i += 1
        if i >= len(a) - 1:
            break
        j = i + 1
        while j < len(a) and a[j] == 0:
            j += 1
        if j >= len(a):
            break
        if i < j:
            a[i], a[j] = a[j], a[i]
            i += 1
    return a


a = [1,0,5,2,0,0,3]
b = [1,0,5,2,0,0,3]
print(move_zeros(a))
print(move_zeros_order(b))

