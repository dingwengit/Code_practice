'''
Given an integer x and an unsorted array of integers, describe an algorithm to
determine whether two of the numbers add up to x. (In this case, say that the
interviewer hates hash tables.)
a = [3,-2, 4, 8, 5, 12,15,18], x=10
method 1
set( 7, 12, 6, 2, 5, 12=12)
method 2
without hashtable or set
1. sort array a1= [-2,3,4,5,8,12,15,18]
2. check sum = a1[0] + a1[-1], then decide move which direction: if sum < x, then a1[1] + a1[-1]
   or if sum > x, then a1[0] + a1[len(a1)-2]
'''
