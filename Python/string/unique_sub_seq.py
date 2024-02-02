'''
given string s and string t, find out how unique sub sequences of s that is t

input: s="aabc", t="abc"
output: 2

edge cases:
s=""
t=""

'''

count = 0

def find_sub_seq(s, t):
    if not t or not s or len(t) == 0 or len(s) == 0:
        return 0

    def find_unique_sub_seq(s, t, i1=0, i2=0):
        global count
        if i2 >= len(t):
            count += 1
            return
        if i1 >= len(s):
            return

        if s[i1] == t[i2]:
            find_unique_sub_seq(s, t, i1+1, i2+1)
        find_unique_sub_seq(s, t, i1 + 1, i2)

    find_unique_sub_seq(s, t)

s="aababxc"
t="abc"
find_sub_seq(s, t)
print(f"count:{count}")
