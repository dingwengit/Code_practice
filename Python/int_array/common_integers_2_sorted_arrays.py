# a1=[2,3,3,5,6,7,7,8,12]
# a2=[5,5,6,8.9.10,10]
# output = [5,6,8]

def find_common(a1, a2):
    i1, i2 = 0, 0
    com = None
    res = []
    while(i1 < len(a1) and i2 < len(a2)):
        if a1[i1] == a2[i2]:
            if com != a1[i1]:
                res.append(a1[i1])
                com = a1[i1]
            i1 += 1
            i2 += 1
        elif a1[i1] > a2[i2]:
            i2 += 1
        else:
            i1 += 1
    return res

a1=[2,3,3,5,6,7,7,8,12]
a2=[5,5,6,8,9,10,10]
print find_common(a1, a2)
