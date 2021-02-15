# given integer array a = [-1, 2, 0, 0, 1, 2, 0]
#
# find out all triplets that sums to 0, no duplicates
# output = [(-1, 0, 1), (-2,0,2), (0,0,0)]
# (1,0,-1) should not appear because of (-1, 0, 1)
#
# the key point is that unique digits in the array matters, so use hashtable
# to store the count
#

def get_dict_count(a, a_dict):
    for item in a:
        if item not in a_dict:
            a_dict[item] = 1
        else:
            a_dict[item] += 1


def find_tuple_sum(a_dict, next_sum, res_tuple):
    for item in a_dict.keys():
        if (next_sum - item) in a_dict:
            if item == next_sum - item:
                if a_dict[item] < 2:
                    continue
            elif a_dict[item] < 1 or a_dict[next_sum - item] < 1:
                continue
            res_tuple.append((item, next_sum - item))


def compare_dict(dic, dic_triplet):
    return not any(key not in dic_triplet or dic[key] != dic_triplet[key] for
               key in dic)


def check_triplet(triplet, res):
    dic = dict()
    get_dict_count(triplet, dic)
    not_found = True
    for item in res:
        dic_triplet = dict()
        get_dict_count(item, dic_triplet)
        if compare_dict(dic, dic_triplet):
            not_found = False
            break
    return not_found


def find_triplets_sum(a, k):
    a_dict = dict()
    res = []
    get_dict_count(a, a_dict)
    for key in a_dict.keys():
        next_sum = k - key
        res_tuple = []
        a_dict[key] -= 1
        find_tuple_sum(a_dict, next_sum, res_tuple)
        a_dict[key] += 1
        for (a1, a2) in res_tuple:
            triplet = (key, a1, a2)
            if check_triplet(triplet, res):
                res.append(triplet)
    return res

print(find_triplets_sum([-1, 2, 0, 0, -1, 2, -3, 0, -4, 1, 5, -2], 0))
