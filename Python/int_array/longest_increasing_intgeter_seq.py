# given an int array, e.g., 3, 5, 17, 4, 8, 12, 9, 10, find the longest
# return count = 5
# increasing sequence (3, 4, 8, 9, 10)

# better solution:
# merge sort has O(nlog(n)) complexity, same as "count_smaller_numbers_after_self.py"
def get_longest_increasing_seq_count(a):
    idx_a = list(enumerate(a))
    counts = [0] * len(a)
    def merge_sort(idx_a):
        if len(idx_a) <= 1:
            return idx_a
        mdl_idx = len(idx_a) // 2
        l_merged = merge_sort(idx_a[:mdl_idx])
        r_merged = merge_sort(idx_a[mdl_idx:])
        return merging_sort(l_merged, r_merged)

    def merging_sort(l_a, r_a):
        i, j, merged, count = 0, 0, [], 0
        while(i<len(l_a) and j<len(r_a)):
            if l_a[i][1] < r_a[j][1]:
                count += 1
                merged.append(l_a[i])
                i += 1
            else:
                counts[r_a[j][0]] += count
                merged.append(r_a[j])
                j += 1

        while(i<len(l_a)):
            merged.append(l_a[i])
            i += 1

        while(j<len(r_a)):
            counts[r_a[j][0]] += count
            merged.append(r_a[j])
            j += 1

        print(f"l_a={l_a} r_a={r_a}, merged={merged}, counts={counts}")
        return merged

    merge_sort(idx_a)
    return max(counts)

print(get_longest_increasing_seq_count(a))