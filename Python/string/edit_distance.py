# find minimum edit distance by given 2 strings, to convert one to the other
# edit -- insert, delete, replace
# str1 = "abc"
# str2 = "cde

def find_min_edit_dist(str1, idx1, str2, idx2):
    if idx1 < 0 and idx2 < 0:
        return 0
    # one of the string has extra chars, let's insert
    if idx1 < 0:
        return idx2 + 1
    if idx2 < 0:
        return idx1 + 1
    if str1[idx1] == str2[idx2]:
        return find_min_edit_dist(str1, idx1-1, str2, idx2-1)
    else:
        # replace, insert / delete on either 1st or 2nd str
        return min(find_min_edit_dist(str1, idx1-1, str2, idx2-1) + 1,
                   find_min_edit_dist(str1, idx1, str2, idx2-1) + 1,
                   find_min_edit_dist(str1, idx1-1, str2, idx2) + 1)

str1 = "bbc"
str2 = "bcb"
print(find_min_edit_dist(str1, len(str1)-1, str2, len(str2)-1))

