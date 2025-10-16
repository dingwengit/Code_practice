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

    # calculate ["1", "*", "2", "-", "3", "*", "4"]
    def get_number(s, idx):
        if idx + 1 >= len(s):
            return int(s[idx]), "end", idx+1
        if s[idx+1] in ["+", "-"]:
            return int(s[idx]), s[idx+1], idx+2
        res = int(s[idx])
        idx += 1
        while idx < len(s) and s[idx] == "*":
            res *= int(s[idx+1])
            idx += 2
        return res, s[idx] if idx < len(s) else "end", idx+1

    def calculate_target(n):
        for item in results:
            idx, res, prev_op = 0, 0, "+"
            while idx < len(item):
                num, op, new_idx = get_number(item, idx)
                if prev_op == "+":
                    res += num
                else:
                    res -= num
                prev_op = op
                idx = new_idx
            if res == n:
                print("".join(item))
                return True
        return False

    exp_s = expand(s)
    insert_operators(exp_s, 1)
    return calculate_target(n)

a="1204"
print(evaluate_target(a, 2))