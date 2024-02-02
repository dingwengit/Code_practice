'''
given an int array a = [12, 6, 32, 5,4,2,3], find the longest consecutive sequence
output = [2,3,4,5,6]

normal cases:
1,2,1,2,4,6,5,7,3
dic: {key a[i]:count}
set: (1, 2)
1 - {1:0}
2 -  because 2-1 =1 in dic but 2+1=3 not dic : {1:1, 2:1}
4 - {4:0}
6 - {6:0}
5 - because both 5 + 1 and 5 -1 are in dic, dic: {4:2, 6:2}
7 - 7-1 in dic: {4:3, 7:3}, delete {6:2}
3 - 3 - 1 and 3 + 1 are in dic, dic: add (2 + 1 + 3)-1 = 6 dic: {1:5, 6:5}, delete {2:1}, delete {4:2}

edge cases:
a = [-1,-1]
a = []
find the max len in dic
'''

def find_max_consecutive_seq(a):
    # assume a contains integers
    dic, numbers = dict(), set()
    if len(a) == 0:
        return 0
    for i in a:
        if i in numbers:
            continue
        else:
            numbers.add(i)
        i1, i2 = i-1, i+1
        print(f"{i} : {dic}")
        if i1 not in dic and i2 not in dic:
            dic[i] = 0
            continue
        if i1 in dic and i2 not in dic:
            cnt = dic[i1]
            dic[i1-cnt], dic[i] = cnt+1, cnt+1
            if cnt != 0:
                del dic[i1]
            continue
        if i1 not in dic and i2 in dic:
            cnt = dic[i2]
            dic[i], dic[i2+cnt] = cnt+1, cnt+1
            if cnt != 0:
                del dic[i2]
            continue
        if i1 in dic and i2 in dic:
            cnt1 = dic[i1]
            cnt2 = dic[i2]
            new_cnt = cnt1 + cnt2 + 2
            dic[i1-cnt1], dic[i2+cnt2] = new_cnt, new_cnt
            if cnt1 != 0:
                del dic[i1]
            if cnt2 != 0:
                del dic[i2]
    print(f"{dic}")
    return max(dic.values()) + 1

print(find_max_consecutive_seq([12,6,32,5,4,2,3]))
