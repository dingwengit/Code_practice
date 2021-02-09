# given string = "azzjskotbz", and partern = "sz", find out the min substring
# that contains each letter in sz (just once), in this case, the answer is "zjs"
# questions:
# any duplicate letters in pattern?
#  " a z z j s k o t b z"
#      i     j

def min_window_substring(s, p):
    in_pattern = set()
    i, j = 0, 0
    while i < len(s) and j < len(s):
        while i + 1 < len(s) and (s[i] == s[i+1] or s[i] not in p):
            i += 1
        if s[i] not in in_pattern:
            in_pattern.add(s[i])
        if i > j:
            j = i
        # handle j
        while len(in_pattern) < len(p):
            j += 1
            if j >= len(s):
                break
            if s[j] in in_pattern: # only once
                while s[i] != s[j]:
                    if s[i] in in_pattern:
                        in_pattern.remove(s[i])
                    i += 1
                i += 1
                break
            if s[j] in p:
                in_pattern.add(s[j])
        if len(in_pattern) == len(p):
            print(s[i:j+1])
            in_pattern.remove(s[i])
            i += 1


s = "sazzzooskotsbzos"
pattern = "soz"
min_window_substring(s, pattern)

