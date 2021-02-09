# convert float into string (up to k decimal):
# input: 234.0045
# output: "234.0045"



def float_to_str(flt, k):
    # convert int to str
    res = []
    a = int(flt)
    if a == 0:
        res.append("0")
    while(a > 0):
        d = a % 10
        res.append("{}".format(d))
        a = int(a / 10)
        # print("d:{} a:{}".format(d, a))
        # return
    res = res[::-1]
    res.append(".")
    # convert decimal to str
    cnt = 1
    flt2 = flt - int(flt)
    while (cnt <= k):
        flt2 *= 10.0
        d = int(flt2) % 10
        res.append("{}".format(d))
        flt2 -= d
        cnt += 1
    return "".join(res)

# print(float_to_str(0.0056, 4))


