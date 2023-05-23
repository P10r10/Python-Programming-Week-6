def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    f = [0, 1]
    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])
    return f[n]


def fib2(n):
    a = 0
    b = 1
    for i in range(1, n + 1):
        c = a + b
        a = b
        b = c
    return (a)
