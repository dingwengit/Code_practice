'''
given an integer array, return a new counts array, where counts[i] is
the number of smaller elements to the right of num[i]

input: [5,2,6,1,3]
res:   [3,1,2,0,0]

1. merge sort

[(5,0),(2,1),(6,2),(1,3),(3,4)] --> (val, index)
counts=[0,0,0,0,0]

merging (5,0),(2,1) -> 5>2, counts[0] = 1 --> (2,1), (5,0)
merging (6,2),(1,3) -> 6>1, counts[2] = 1 --> (1,3),(6,2)
merging (3,4), (1000, 5) -> counts[5] = 1 --> (3,4), (1000,5)

merging (2,1) (1,3) ->
merging (5,0), (2,1) ->

https://towardsdatascience.com/self-balancing-binary-search-trees-101-fc4f51199e1d

AVL tree (from right to left of arr):
              3 (1)
            /
           1 (0)
insert: 6
              3 (1)
            /    \
           1 (0)  6(2)

insert: 2
              3 (1)
            /    \
           1 (0)  6(2)
'''


class Solution:
    def __init__(self, nums):
        self.nums = nums

    def countSmaller(self):
        indexed_nums = list(enumerate(self.nums))
        self.counts = [0] * len(self.nums)
        self.merge_sort(indexed_nums)
        return self.counts

    def merge_sort(self, indexed_nums):
        if len(indexed_nums) <= 1:
            return indexed_nums

        mid = len(indexed_nums) // 2
        left_half = self.merge_sort(indexed_nums[:mid])
        right_half = self.merge_sort(indexed_nums[mid:])

        return self.merge(left_half, right_half)

    def merge(self, left_half, right_half):
        merged = []
        i, j = 0, 0
        right_count = 0

        while i < len(left_half) and j < len(right_half):
            # If the element from the left half is smaller or equal,
            # it means it is smaller than all the elements we've skipped
            # over in the right half so far.
            if left_half[i][1] <= right_half[j][1]:
                self.counts[left_half[i][0]] += right_count
                merged.append(left_half[i])
                i += 1
            # If the element from the right half is smaller,
            # it is a smaller number to the right of every remaining
            # element in the left half. We track this with `right_count`.
            else:
                merged.append(right_half[j])
                right_count += 1
                j += 1

        # Add any remaining elements from the left half
        while i < len(left_half):
            self.counts[left_half[i][0]] += right_count
            merged.append(left_half[i])
            i += 1

        # Add any remaining elements from the right half
        while j < len(right_half):
            merged.append(right_half[j])
            j += 1

        print(f"left_half={left_half}, right_half={right_half}, merged={merged}, counts={self.counts}")

        return merged

s = Solution([5,2,6,1,3])

print(s.countSmaller())