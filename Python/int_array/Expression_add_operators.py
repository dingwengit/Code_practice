'''
given a string that contains only digits 0-9 and a target value,
return # of posibilities to add binary operators "+, -, *"
between the 2 adjacent so they evaluate to the target value
If non exists, return -1

input: "123", target = 6
output: ["1+2+3", "1*2*3"]

input: "123", target = 7
output: ["1+2*3"]
      s  = "1+2*3"
     idx = 0
    res = 0, prev_operator='+'
  n, operator = process_idx(idx) -> if s[idx+1] == '+' or '-' return s[idx], operator='+' or '-' else s[idx]*s[idx+2], idx+=2
    res = res (prev_operator) n
    prev_operator = operator

input: "00", target = 0
output: ["0+0", "0-0", "0*0"]
'''

#import copy

def evaluate_target(s, n):
    operators = ["+","-","*"]
    results = []

    # change "1234" into ["1", " ", "2", " ", "3", " ", "4"]
    def expand(s):
        s1 = []
        for c in s:
            s1.append(c)
            s1.append(" ")
        if len(s1) > 0: # remove last empty space
            del s1[-1]
        return s1

    # change ["1", " ", "2", " ", "3", " ", "4"]
    # into ["1", "+/-/*", "2", "+/-/*", "3", "+/-/*", "4"]
    def insert_operators(exp_s, idx):
        if idx >= len(exp_s):
            results.append(exp_s.copy())
            return

        for op in operators:
            exp_s[idx] = op
            insert_operators(exp_s, idx + 2)

    # from ["1", "*", "2", "-", "3", "*", "4"]
    # calculate all "*" first, and form into a new array [2,"-",12]
    def get_number(s):
        i, res = 0, []
        # print(f"s={s}")
        while(i < len(s)):
            if i + 1 == len(s):
                res.append(int(s[i]))
                break;
            if (s[i] in ["+", "-"]):
                res.append(s[i])
                i += 1
                continue
            if s[i+1] in ["+", "-"]:
                res.append(int(s[i]))
                res.append(s[i+1])
                i += 2
            elif s[i+1] == "*":
                # print(f"s[i]={s[i]}, i={i}")
                n = int(s[i])
                while(i+1 < len(s) and s[i+1] == "*"):
                    n *= int(s[i+2])
                    i += 2
                res.append(n)
                i += 1
        i, n = 0, res[0]
        # print(f"res={res}")
        while i + 1 < len(res):
            if res[i+1] == "+":
                n += res[i+2]
            if res[i+1] == "-":
                n -= res[i+2]
            i += 2
        return n

    def calculate_target(n):
        for item in results:
            res = get_number(item)
            if res == n:
                print("".join(item))
                return True
        return False

    exp_s = expand(s)
    insert_operators(exp_s, 1)
    return calculate_target(n)

a="1214"
print(evaluate_target(a, 9))