# == questions: give an integer array A, an inversion means a[i]<a[j]
# when i>j, write a function
# to count total inversions in the array
# a = [5, 2, 1, 4], inversions = 4

# this is O(n^2) solution
def count_inversions(a):
    return sum(1 if a[i] > a[j] else 0 for i in range(len(a))
                for j in range(i + 1, len(a)))

# Find a solution of O(nlog(n)) solution, which is the same as count_smaller_numbers_after_self.py


a = [5, 2, 1, 4]
print(count_inversions(a))

