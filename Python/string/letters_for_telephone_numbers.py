phone_mapping = {
'0':[],
'1':[],
'2':['a', 'b', 'c'],
'3':['d', 'e', 'f'],
'4':['g', 'h', 'i'],
'5':['j', 'k', 'l'],
'6':['m', 'n', 'o'],
'7':['p', 'q', 'r', 's'],
'8':['t', 'u', 'v'],
'9':['w', 'x', 'y', 'z']
}

def print_phone_letters(a, m, idx, res):
    if idx >= len(a):
        print ''.join(res)
        returnw

    letters = m[a[idx]]
    if len(letters) > 0:
        for c in letters:
            res[idx] = c
            print_phone_letters(a, m, idx + 1, res)
    else:
        print_phone_letters(a, m, idx + 1, res)


a = '415'
res = [''] * len(a)
print_phone_letters(a, phone_mapping, 0, res)