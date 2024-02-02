#!/usr/bin/env python

'''
given a string and a list of words
find all starting indices that of substring that is a concatenation of each work in the list exact once
and without any invervening characters

input: s = "barfootthefoobarman", words = ["bar", "foo"]
output: = [0,9], or [9,0]
'''

def get_prefix(s, words, found_words):
    res = []
    for idx in range(len(words)):
        if idx not in found_words:
            if s.startswith(words[idx]):
                res.append(idx)
    return res


def check_words(s, words, found_words):
    word_idx = get_prefix(s, words, found_words)
    for idx in word_idx:
        if idx in found_words:
            continue
        found_words.add(idx)
        if len(found_words) == len(words):
            return True
        if check_words(s[len(words[idx]):], words, found_words):
            return True
        found_words.remove(idx)
    return False


def find_indices(s, words, res):
    for idx in range(len(s)):
        found_words = set()
        if check_words(s[idx:], words, found_words):
            res.append(idx)


res = []
s = "barfoothefoosfoosfoobarman"
words = ["bar", "foo"]
find_indices(s, words, res)
print(res)