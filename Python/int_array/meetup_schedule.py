'''
A start-up owner is looking to meet new investors to get some funds for the company. Each investor has a tight schedule that the owner has to respect.
Given the schedules of the days investors are available, determine how many meetings the owner can schedule. Note that the owner can only have one meeting per day.
The schedules consist of two integer arrays: firstDay, and lastDay, aligned by index. Each element in the array firstDay represents the first day an investor is available, and each element in lastDay represents the last day an investor is available, both inclusive.
xample:
firstDay = [1,2,3,3,3]
lastDay= [2,2,3,4,4]
    There are 5 investors [I-0, I-1, I-2, I-3, I-4]
    The investor I-0 is available from day 1 to day 2 inclusive [1, 2]
    The investor I-1 is available in day 2 only [2, 2]. The investor I-2 is available in day 3 only [3, 3]
    The investors I-3 and I-4 are available from day 3 to day 4 only [3, 4]
    The owner can only meet 4 investors out of 5 :
    I-0 in day 1, I-1 in day 2, I-2 in day 3 and I-3 in day 4. The graphic below shows the scheduled meetings in green and blocked days are in gray.

     day:  1  2  3  4  5  6  7  8  9
idx:
0          -  -  -
1             -
2          -
3                -  -
4             -  -  -  -
5                   -  -  -

'''