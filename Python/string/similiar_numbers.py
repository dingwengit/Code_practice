# Question
#
# Count the number of ways to reorder a number's digits while maintaining specific properties.
#
#
#
# Two numbers are considered similar if:
#
#     They have the same frequency of each digit
#     Neither has leading zeros
#
# Given two strings representing long integers a and b:
#
#     If a and b are similar, find the total number of numbers similar to a.
#     If a and b are not similar, find the total number of numbers similar to b.
#
#
#
# Example
#
#     If a = "112" and b = "121", they are similar (both have two 1's and one 2). Count the 3 numbers similar to a: {"112", "121", "211"}.
#     If a = "11" and b = "223", they are not similar. Count the 3 numbers similar to b: {"223", "232", "322"}.
#
#
#
# Function Description
#
# Complete the function findSimilar in the editor with the following parameter(s):
#
#     string a:  a string representation of a long integer
#
#     string b:  a string representation of a long integer
#
#
#
# Returns
#
#      long int: the number of integers similar to a or b, as required
import math

def findSimilar(a, b):

    # note that if a and b are similar, permutations of a and b are the same
    # always work on b

    # count the digits of each type
    counts = [0] * 10
    for c in b:
        counts[int(c)] += 1

    # calculate the gross number of permutations
    ans = 1
    for v in counts:
        if v > 0:
            ans *= math.factorial(v)
    print(f"ans={ans}")
    ans = math.factorial(len(b)) // ans
    print(f"ans={ans}")

    # count the permutations that start with 0
    if counts[0] > 0:
        ans2 = 1
        counts[0] -= 1
        for v in counts:
            if v > 0:
                ans2 *= math.factorial(v)
        ans2 = math.factorial(len(b) - 1) // ans2
    else:
        ans2 = 0

    ans -= ans2
    return ans

print(findSimilar("1121", "1211"))