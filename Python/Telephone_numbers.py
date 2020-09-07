#!/usr/bin/env python

# given telephone number 2068920023, each digit could map to 0 or several
# letters
# print out all possible combinations of characters for the phone number

#       2 0 6 8 9 2 0 0 2 3
# idx   0
#     [c1, c2, c3]

p_n_map = {
    "0": [''],
    "1": [''],
    "2": ['a', 'b', 'c'],
    "3": ['d', 'e', 'f'],
    "4": ['g', 'h', 'i'],
    "5": ['j', 'k', 'l'],
    "6": ['m', 'n', 'o'],
    "7": ['p', 'q', 'r', 's'],
    "8": ['t', 'u', 'v'],
    "9": ['w', 'x', 'y', 'z'],
}

def get_letters(p_n):
    return p_n_map[p_n]

def print_phone_number_letters(phone, res, idx):
    if idx >= len(phone):
        print ''.join(res)
        return

    for ch in get_letters(phone[idx]):
        res[idx] = ch
        print_phone_number_letters(phone, res, idx+1)

if __name__ == "__main__":
    phone = "206"
    res = [' '] * len(phone)

    print_phone_number_letters(phone, res, 0)
