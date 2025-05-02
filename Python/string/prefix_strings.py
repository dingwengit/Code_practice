# given a list of strings and a word prefix
# return a list of strings that start with given prefix
# words = ["alex","anton","anastasiya","denis"]
# prefix
# a -> alex, anton, anastasiya
# an -> anton, anastasiya

def print_str(words, prefix):
    m = len(prefix)
    for w in words:
        if len(w) >= m and prefix == w[:m]:
            print(w)


print_str(["alex","anton","anastasiya","denis"], "anast")
