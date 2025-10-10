# given a string, print out all docompositions of the string where each
# sub-str is palindrome
# input = "0204451881"
# output = 020, 44, 5, 1881
#          0,2,0,44,5,1,88,1


def palindrome_decompsition(str, st, res):
    if st == len(str):
        print(res)

    for idx in range(st+1, len(str)+1):
        prefix = str[st:idx]
        if prefix == prefix[::-1]: # palindrome
            res.append(prefix)
            palindrome_decompsition(str, idx, res)
            del res[-1]

str = "0204451881"
res = []
palindrome_decompsition(str, 0, res)
