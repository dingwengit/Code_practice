# given a string, print out all possible words that make up the entire string
# e.g., s = "onpinsandneedles"
# result:
# ['on", "pin", "sand", "needles"],
# ['on", "pins", "sand", "needles"]

dictionary = ["on", "pin", "pins", "and", "sand", "needles"]


def sentence_break(s, res):
    if s == '':
        print res
        return

    for i in range(1, len(s) + 1):
        found = False
        if s[:i] in dictionary:
            found = True
            # print s[:i] + " -- " + s[i:]
            res.append(s[:i])
            sentence_break(s[i:], res)
        if found and len(res) > 0:
            del res[len(res) -1]


sentence_break("onpinsandpinsandneedles",[])
