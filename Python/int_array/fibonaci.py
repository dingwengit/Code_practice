# f(i) = f(i-1) + f(i-2)

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


def fibonacci_2(n, a):
    a[1] = 1
    for i in range(2, n+1):
        a[i] = a[i-1] + a[i-2]
    return a[n]

n = 4
a = [0] * (n+1)
print fibonacci(n)
print fibonacci_2(n, a)
