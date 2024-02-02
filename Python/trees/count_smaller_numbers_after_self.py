'''
given an integer array, return a new counts array, where counts[i] is the number of smaller
elements to the right of num[i]

input: [5,2,6,1]
output: [2,1,1,0]

https://towardsdatascience.com/self-balancing-binary-search-trees-101-fc4f51199e1d

AVL tree (from right to left of arr):
              6 (1)
            /
           1 (0)
insert: 2
              6 (2)
            /
           1 (0)
            \
             2
              6 (2)
            /
           2 (1)
          /
         1 (0)

'''