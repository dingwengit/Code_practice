'''
given s1, and s2, and s3, find whether s3 is formed by the interleaving of s1 and s2

input: s1: "abcd", s2:"efgh", s3: "aebcfghd"
output: True

input: s1: "abcd", s2:"efgh", s3: "aebdfghc"
output: False

edge cases:
s1: "", s2: "", s3: ""
'''

def check_string_interleaving(s1, s2, s3):
    if not s1 and not s2 and not s3:
        return True
    # check other edge cases
    if len(s1) + len(s2) != len(s3):
        return False

    def check_interleaving(s1, s2, s3, i1=0, i2=0, i3=0):
        if i1 >= len(s1) and i2 >= len(s2) and i3 >= len(s3):
            return True
        # print(f"i1:{i1},i2:{i2},i3:{i3}")
        if i1<len(s1) and s3[i3] == s1[i1] and i2<len(s2) and s3[i3] == s2[i2]:
            return check_interleaving(s1,s2,s3,i1+1,i2,i3+1) or check_interleaving(s1,s2,s3,i1,i2+1,i3+1)
        if i1<len(s1) and s3[i3] == s1[i1]:
            return check_interleaving(s1,s2,s3,i1+1,i2,i3+1)
        if i2<len(s2) and s3[i3] == s2[i2]:
            return check_interleaving(s1,s2,s3,i1,i2+1,i3+1)
        return False

    return check_interleaving(s1,s2,s3)


s1,s2,s3 = "aacad","acah","aacacadah"
print(check_string_interleaving(s1, s2, s3))
