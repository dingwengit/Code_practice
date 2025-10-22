'''
Question:
Given a list of intervals where each interval is a pair of integers [start, end] that
are sorted by start time
write a function to merge all overlapping intervals and
return a list of the merged intervals sorted by start time.

Example Input: [[1,3], [3,7], [8,10], [9,12],[15,18]]
Expected Output: [[1,7], [8,12], [15,18]]

method:
overlap means "end" of idx >= a[idx+1][0]
if no overlap, save [st, end] -> out

                              [[1,3], [3,7], [8,10], [9,12],          [15,18]]
idx                             0       1      2       3               4
[st,end] is overlap w idx+1?    T       F      T       F               F
st       1                      1       8      8       15
end      3                 max(3, 7)   10   max(10, 12) 18
out                             [] -> [1,7]->[1,7] ->[[1,7],[8,12]] ->[[1,7], [8,12], [15, 18]]

try the above method on Input: [[1,13], [3,7], [8,10], [9,12],[15,18]]

'''