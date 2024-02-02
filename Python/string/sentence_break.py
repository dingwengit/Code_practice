# given a string, print out all possible words that make up the entire string
# e.g., s = "onpinsandneedles"
# result:
# ['on", "pin", "sand", "needles"],
# ['on", "pins", "and", "needles"]

dictionary = ["on", "pin", "pins", "and", "sand", "needles"]


def sentence_break(s, res):
    if s == '':
        print(res)
        return

    for i in range(1, len(s) + 1):
        if s[:i] in dictionary:
            # print s[:i] + " -- " + s[i:]
            res.append(s[:i])
            sentence_break(s[i:], res)
            del res[len(res) -1]


def sentence_break2(s, st=0, res=[]):
    if st >= len(s):
        print(res)
        return

    for idx in range(st+1, len(s)+1):
        if s[st:idx] in dictionary:
            res.append(s[st:idx])
            sentence_break2(s, idx, res)
            del res[len(res) -1]

# sentence_break("onpinsandneedles",[])
# sentence_break("onpinsan",[])
sentence_break2("onpinsandneedles")
# sentence_break2("onpinsan", 0, [])
