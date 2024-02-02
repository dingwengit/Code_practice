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


def print_phone_letters(s, m, idx, res):
    if idx >= len(s):
        print(''.join(res))
        return

    candidates = m[s[idx]]
    for c in candidates:
        res[idx] = c
        print_phone_letters(s, m, idx+1, res)
    if len(candidates) == 0:
        res[idx] = ''
        print_phone_letters(s, m, idx+1, res)


s = '415'
res = [''] * len(s)
print_phone_letters(s, phone_mapping, 0, res)