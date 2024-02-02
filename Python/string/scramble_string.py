'''
Given two strings S1 and S2 of equal length, the task is to determine if S2 is a scrambled form of S1.
Scrambled string:
Given string str, we can represent it as a binary tree by partitioning it into two non-empty substrings recursively.
Note: Scrambled string is not same as an Anagram
Below is one possible representation of str = “coder”:


    coder
   /    \
  co    der
 / \    /  \
c   o  d   er
           / \
          e   r

To scramble the string, we may choose any non-leaf node and swap its two children.
Suppose, we choose the node “co” and swap its two children, it produces a scrambled string “ocder”.


    ocder
   /    \
  oc    der
 / \    /  \
o   c  d   er
           / \
          e   r

Thus, “ocder” is a scrambled string of “coder”.
Similarly, if we continue to swap the children of nodes “der” and “er”, it produces a scrambled string “ocred”.


    ocred
   /    \
  oc    red
 / \    /  \
o   c  re  d
       / \
      r   e

Thus, “ocred” is a scrambled string of “coder”.
Examples:

    Input: S1=”coder”, S2=”ocder”
    Output: Yes
    Explanation:
    “ocder” is a scrambled form of “coder”
    Input: S1=”abcde”, S2=”caebd”
    Output: No
    Explanation:
    “caebd” is not a scrambled form of “abcde”
'''

# node that we must have at least one char in its subtree, so we cannot check S1 and S2 as a whole to see
# if they are anagram or scrambled string
# solution: there must be an index that satisfy (1) [1,len(s)] that S1[0..idx] is scrambled / anagram of S2[0..idx] and
# S1[idx+1.. len(s)] is scrambled of S2[idx+1...len(s)]
# or (2) S1[0..idx] is scrambiled of S2[len(s) - idx, len(s)] and S1[len(s) - idx, len(s)] is scrambled of S2[0..idx]

def is_scrambled(s1, s2, map=dict()):
    if len(s1) != len(s2):
        return False
    n = len(s1)
    if n == 0 or s1 == s2:
        return True

    if s1+"-"+s2 in map:
        return map[s1+"-"+s2]

    if sorted(s1) != sorted(s2): # if not anagram then not scrambled
        map[s1 + "-" + s2] = False
        return False

    for i in range(1, n):
        if is_scrambled(s1[:i], s2[:i]) and is_scrambled(s1[i:], s2[i:]):
            map[s1 + "-" + s2] = True
            return True
        if is_scrambled(s1[len(s1)-i:len(s1)], s2[:i]) and is_scrambled(s1[:i], s2[len(s2)-i:len(s2)]):
            map[s1 + "-" + s2] = True
            return True

    map[s1 + "-" + s2] = False

    return False

S1="great"
S2="rgtae"
print(is_scrambled(S1, S2))
S1="abcde"
S2="caebd"
print(is_scrambled(S1, S2))
