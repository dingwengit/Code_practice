# == questions: give an integer array A, an inversion means a[i]<a[j] when i>j, write a function
#               to count total inversions in the array
# a = [5, 2, 1, 4], inversions = 4

def count_inversions(a):
    return sum(1 if a[i] > a[j] else 0 for i in range(len(a))
                for j in range(i + 1, len(a)))

a = [5, 2, 1, 4]
print(count_inversions(a))

