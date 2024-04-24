'''
       top
     A C I D
     T     A
left O     R right
     M A R K
       bot

       top
     t e s t
     e     e
left a     e right
     s e e n
       bot

input: 4-letter words ["teen", "acid", "atom", "teas", "word", "seen", "mark", "dark", "test"]

output:
print out all squares
//top, right, bottom, left

acid, dark, mark, atom
'''

# method 1: loop each word in top,right,bottom,left positions and print out the final square
def Get_all_squares(words):
    for i, top in enumerate(words):
        visited = set()
        visited.add(i)
        for j, right in enumerate(words):
            if j in visited or not top[3] == right[0]:
                continue
            visited.add(j)
            for k, bottom in enumerate(words):
                if k in visited or not bottom[3] == right[3]:
                    continue
                visited.add(k)
                for m, left in enumerate(words):
                    if m in visited or not left[3] == bottom[0] or not left[0] == top[0]:
                        continue
                    print(f"{top}-{right}-{bottom}-{left}")

# method 2
def print_squares(words):
    visited = set()
    for idx in range(len(words)):
        res = [(idx, words[idx])]
        find_all_squares(words, res, visited)


def add_square(words, res, visited):
    used_idx = set()
    top, right, bottom, left = None, None, None, None
    visit = ''
    for i in range(len(res)):
        idx, word = res[i]
        used_idx.add(idx)
        visit += f"{idx}-"
        if i == 0:
            top = word
        if i == 1:
            right = word
        if i == 2:
            bottom = word

    for i, w in enumerate(words):
        if i in used_idx or visit + f"{i}" in visited:
            continue
        found = False
        if bottom != None:
            found = w[0] == top[0] and w[3] == bottom[0]
        elif right != None:
            found = w[3] == right[3]
        elif top != None:
            found = w[0] == top[3]
        if found:
            res.append((i, w))
            visited.add(visit + f"{i}")
            return i
    return -1


def find_all_squares(words, res, visited):
    idx = add_square(words, res, visited)
    if idx == -1:
        del res[len(res)-1]
        if len(res) < 1:
            return
    elif len(res) == 4:
        print(res)
        del res[len(res)-1]
    find_all_squares(words, res, visited)


words = ["teen", "acid", "atom", "teas", "word", "seen", "mark", "dark", "test"]
# print_squares(words)
Get_all_squares(words)