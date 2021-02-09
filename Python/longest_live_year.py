# given a group of people with birth year and death year
# write a function to find out the longest living year with the most people

people = [(1960, 2010), (1930, 2000), (1990, 2020), (1970, 2018)]
# |-----|
# |-----|
#       |-----|
#             |-----|


def find_longest_live_year(people):
    map = {}
    for p in people:
        for year in range(p[0], p[1] + 1):
            if year in map:
                map[year] += 1
            else:
                map[year] = 1
    lly = 0
    max_people = 0
    for y in map.keys():
        if map[y] > max_people:
            max_people = map[y]
            lly = y
    print "lly={}, max_people={}".format(lly, max_people)


find_longest_live_year(people)
