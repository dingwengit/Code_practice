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

def sentence_break2(s, idx, res):
    if idx >= len(s):
        print(res)
        return

    for i in range(idx+1, len(s)+1):
        if s[idx:i] in dictionary:
            res.append(s[idx:i])
            sentence_break2(s, i, res)
            del res[len(res) -1]

# sentence_break("onpinsandneedles",[])
# sentence_break("onpinsan",[])
sentence_break2("onpinsandneedles", 0, [])
# sentence_break2("onpinsan", 0, [])
