'''
given an int array a = [2, 6, 3, 5, 4, 6, 3,9,8,7,8,9],
find the longest consecutive sequence
output = [6,7,8,9] // keep the same order in orignal array?

          [2, 6,  3, 5, 4, 6, 3,9,8,7,8,9]
ht        2:(3,0)
              6:(1,1)
                  3:(1,2) (3-1=2) so ht[2] +=1
                     5:(2,3)
                        4:(1,4) (4-1=3, 3-1=2, 2-1 not in ht, so jt[2] +=1)
                           6:(1,5) (6-1=5, 5-1=4, but idx of 5 is 3, idx of 4 is 4, ht[5] +=1

                           ....
'''