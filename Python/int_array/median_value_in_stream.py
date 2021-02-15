import heapq

# given a stream of integers, keep return the medium value of current seen
# a = [5,4,3,6,7,8,1,2,9]
#
# read 5 min_heap [5] max_heap [] --> pushpop on max_heap, then push min_heap
# read 4 min_heap [5] max_heap [4] --> pushpop, pop on min_heap --> push
# max_heap
# read 3 min_heap [4, 5]   max_heap [3] --> pushpop
# read 6 min_heap [5, 6]   max_heap [4, 3] --> pushpop


def find_medium_stream(a):
    min_heap, max_heap = [], []
    for data in a:
        heapq.heappush(min_heap, -1 * heapq.heappushpop(max_heap, -1 * data))
        if len(min_heap) > len(max_heap) + 1:
            heapq.heappush(max_heap, -1 * heapq.heappop(min_heap))

        medium = (min_heap[0] + (-1 * max_heap[0])) / 2 if len(min_heap) == \
                                                         len(max_heap) else \
            min_heap[0]
        print("{} - {} : {}".format(medium, min_heap, max_heap))

find_medium_stream([5,4,3,6,7,8,1,2,9])

