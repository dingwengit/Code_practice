import heapq

# given a stream of integers, keep return the medium value of current seen
# a = [5,4,3,6,7,8,1,2,9]
#
# read 5 min_heap [5] max_heap [] --> pushpop on max_heap, then push min_heap
# * read 4 min_heap [4, 5] max_heap [] --> pushpop on max_heap, then push min_heap
#        min_heap [5] max_heap [4] --> pushpop, pop on min_heap --> push max_heap --> 5>4
# read 3 min_heap [4, 5]   max_heap [3] --> pushpop  --> 4>3
# read 6 min_heap [5, 6]   max_heap [4, 3] --> pushpop --> 5>4
# read 7 min_heap [5, 6, 7]  max_heap [4, 3] --> pushpop
# read 8 min_heap [6, 7, 8]  max_heap [5, 4, 3] --> pushpop 6 > 5
# * read 8 min_heap [1, 6, 7, 8]  max_heap [5, 4, 3] --> pushpop --> because 1 < 5, let's do push pop
# read 8 min_heap [6, 7, 8]  max_heap [5, 4, 3, 1] --> pushpop --> because 1 < 5, let's do push pop
#
#

def find_medium_stream(a):
    min_heap, max_heap = [], []
    for data in a:
        heapq.heappush(min_heap, data)
        if len(min_heap) > len(max_heap) + 1 or \
                (len(min_heap) > 0 and len(max_heap) > 0 and min_heap[0] < -1 * max_heap[0]):
            heapq.heappush(max_heap, -1 * heapq.heappop(min_heap))
        if len(min_heap) < len(max_heap):
            heapq.heappush(min_heap, -1 * heapq.heappop(max_heap))

        if len(max_heap) == len(min_heap):
            medium = (min_heap[0] + (-1 * max_heap[0])) / 2
        elif len(max_heap) > len(min_heap):
            medium = (-1 * max_heap[0])
        else:
            medium = min_heap[0]
        # print("{} - {} : {}".format(medium, min_heap, max_heap))

find_medium_stream([5,4,3,6,7,8,1,2,9])

