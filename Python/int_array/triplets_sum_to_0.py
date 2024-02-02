# given integer array a = [-1, 2, 0, 0, 1, 2, 0]
#
# find out all triplets that sums to 0, no duplicates
# output = [(-1, 0, 1), (-2,0,2), (0,0,0)]
# (1,0,-1) should not appear because of (-1, 0, 1)
# save results into dict()
# [{1:2, -2:1}, {0:3}, ...]
#
# the key point is that unique digits in the array matters, so use hashtable
# to store the count
#

def found_in_hash(tripple, res_hash):
    dic = dict()
    for item in tripple:
        if item in dic:
            dic[item] += 1
        else:
            dic[item] = 0

    for res in res_hash:
        found_item = True
        for key in dic.keys():
            if key not in res:
                found_item = False
                break
            if dic[key] != res[key]:
                found_item = False
                break
        if found_item:
            return True

    res_hash.append(dic)
    return False


def get_tripples(a):
    res = set()
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            for k in range(j+1, len(a)):
                if a[i]+a[j]+a[k] == 0 and (a[i], a[j], a[k]) not in res:
                    res.add((a[i], a[j], a[k]))
    res_hash = []
    for tripple in res:
        if not found_in_hash(tripple, res_hash):
            print(tripple)



# print(find_triplets_sum([-1, 2, 0, 0, -1, 2, -3, 0, -4, 1, 5, -2], 0))
a = [-1, 2, 0, 0, 1, -2, 0, 3]
get_tripples(a)