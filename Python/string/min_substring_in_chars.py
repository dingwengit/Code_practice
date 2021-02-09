# given unique char array = ['x', 'y', 'z'], and input string = "xyyzyyzx",
# find the min substring that each char in char array just show up once
#      "x x y x x z z y y z z x"
#         i       j

# assumption: no other letters in the array

def decrease_cnt(c, dic):
    if c in dic:
        dic[c] -= 1
        if dic[c] == 0:
            del dic[c]


def increase_cnt(c, dic):
    if c in dic:
        dic[c] += 1
    else:
        dic[c] = 1


def min_substr(arr, s):
    sub_dict = dict()
    i, j = 0, 0
    while j < len(s) and i < len(s):
        # print("i:{} j:{} sub_dict: ()".format(i, j, sub_dict))
        while i < len(s) - 1 and s[i] == s[i+1]:
            decrease_cnt(s[i], sub_dict)
            i = i + 1
        if i >= j:
            j = i
            increase_cnt(s[i], sub_dict)
        while len(sub_dict) < len(arr):
            j += 1
            if j >= len(s):
                break
            increase_cnt(s[j], sub_dict)
        if len(sub_dict) == len(arr):
            print(s[i:j+1])
            decrease_cnt(s[i], sub_dict)
            i = i + 1

min_substr(['x','y','z'], "xyyzyyzzx")
