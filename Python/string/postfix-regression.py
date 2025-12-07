'''
The way to write arithmetic expression is known as a notation.
Postfix Notation - this notation style is known as Reversed Polish Notation.
In this notation style, the operator is postfixed to the operands i.e.,
the operator is written after the operands.
For example, ab+. This is equivalent to its infix notation a + b.

On input you will receive a string of characters separated with ','
String represents Postfix Notation.
Write a program which can return result of expression.
Example:
 
for input like this "4,2,-" program expected to return result is 2
for input like this "1,2,+,3,*,4,-" ((1+2)*3)-4)  expected result is 5

restrictions:
assume that input string is valid arithmetic expression, no syntax errors

Solutions:
        "1, 2,+,3,*,4,-"
idx           +
stack:  [1,2]
stack[0]"operator"stack[1] -> res -> stack[0]
'''

def arithmetic_expression(s):
    arr = s.split(",")

    def cal_expr(arr):
        stack = []
        for c in arr:
            if c in ["+","-","*","/"]:
                if len(stack) != 2:
                    raise Exception(f"Invalid expression {arr}")
                if c == "+":
                    stack[0] = stack[0] + stack[1]
                if c == "-":
                    stack[0] = stack[0] - stack[1]
                if c == "*":
                    stack[0] = stack[0] * stack[1]
                if c == "/":
                    stack[0] = stack[0] // stack[1]
                del stack[-1]
            else:
                stack.append(int(c))
        return stack[0]

    return cal_expr(arr)

s = "1,2,+,3,*,4,-"
print(arithmetic_expression(s))