# given unique char array = ['x', 'y', 'z'], and input string = "xyyzyyzx",
# find the min substring that each char in char array just show up once
#      "x x y x x z z y y z z x"
#         i       j

# assumption: no other letters in the array


def min_substr(arr, s):
    sub_set = set()
    res = None
    min_len = len(s)
    i, j = 0, 0
    while j < len(s) and i < len(s):
        #print("i:{} j:{} sub_dict: ()".format(i, j, sub_set))
        # first update start index i
        while i < len(s) - 1 and (s[i] == s[i+1] or s[i] not in arr):
            i = i + 1
        if s[i] not in sub_set and s[j] in arr:
            sub_set.add(s[i])
        if i >= j:
            j = i
        # now update end index j
        while len(sub_set) < len(arr):
            j += 1
            if j >= len(s):
                break
            if s[j] not in sub_set and s[j] in arr:
                sub_set.add(s[j])
            elif s[j] in sub_set: # now need to remove s[j] from sub_set
                while(s[i] != s[j]):
                    if s[i] in sub_set:
                        sub_set.remove(s[i])
                    i += 1
                i += 1
                break
        if len(sub_set) == len(arr):
            if min_len > j + 1 - i:
                min_len, res = j + 1 - i, s[i:j+1]
                print("res:{}".format(s[i:j+1]))
            if s[i] in sub_set:
                sub_set.remove(s[i])
            i = i + 1
    return res

print(min_substr(['x','y','z'], "yyazxazxyczyyazzx"))

