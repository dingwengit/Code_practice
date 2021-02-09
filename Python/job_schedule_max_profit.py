# given array of schedules, consists of start-time and end-time, each job
# has a profit, write a function to find out the max possible profit

# input: a=[(1,3,5), (2,4,3), (3,5,2), (2,5,4), (1,6,5), (2,7, 6), (6, 7, 2)]
#
# |----2----| |----15----| |-----18---| |---21-----|
#       |----4----| |---6-----| |---19-----| |---23-----|
#
# jobs_st = {{1:[(1,3,5)]}, {2:[(2,4,3), (2,5,4)]}, ...}
# jobs_end = {{3:[(1,3,5)]}, {5:[(3,5,2), (2,5,4)]}, ...}
import sys


class job:
    def __init__(self, st, end, profit):
        self.st, self.end, self.profit = st, end, profit


def find_max_profit(jobs):
    jobs_st = dict()
    jobs_end = dict()
    new_jobs = []
    # convert to class
    for st, end, profit in jobs:
        new_jobs.append(job(st, end, profit))

    start = sys.maxsize
    end = 0
    # build jobs_st, jobs_end
    for data in new_jobs:
        if data.st not in jobs_st:
            jobs_st[data.st] = [data]
        else:
            jobs_st[data.st].append(data)
        start = min(start, data.st)

        if data.end not in jobs_end:
            jobs_end[data.end] = [data]
        else:
            jobs_end[data.end].append(data)
        end = max(end, data.end)

    cur_profit = 0
    for i in range(start, end+1):
        # *** need to check jobs_end first ***
        if i in jobs_end:
            for data in jobs_end[i]:
                cur_profit = max(cur_profit, data.profit)
        if i in jobs_st:
            for data in jobs_st[i]:
                data.profit += cur_profit
    print("max_profit: {}".format(cur_profit))

find_max_profit([(1,2,5), (2,4,3), (3,5,7), (2,5,4)])