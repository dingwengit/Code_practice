#!/usr/bin/env python
from array import *
import heapq

# given a set of [start-time, end-time] booking of meeting rooms, write a
# function to return the max number of meeting rooms needed
# e.g., [1, 3], [2, 4], [3, 5], return 2
#   1: (1,3)
#   2: (1,3), (2,4)
#   3: (2,4), (3,5)
#   4: (3,5)

# assume, the set is sorted by start-time

def max_rooms(t):
    max_rooms = 0
    slots = []
    for slot in t:
        st, end = slot[0], slot[1]
        # 1. start
        if len(slots) == 0:
            heapq.heappush(slots, (end, st)) # minheap by default -
            # meaning slots is in ascent order
            max_rooms = max(1, max_rooms)
            continue
        # 2 check if start time is later than current min_end time
        min_end = slots[0][0]
        if st < min_end: # new start is less than current min_end
            heapq.heappush(slots, (end, st))
            max_rooms = max(len(slots), max_rooms)
        else:
            while st >= min_end:
                heapq.heappop(slots)
                if len(slots) > 0:
                    min_end = slots[0][0]
                else:
                    break

    return max_rooms

if __name__ == '__main__':
    t = [[1,6], [2,3], [3,4]]
    print(max_rooms(t))