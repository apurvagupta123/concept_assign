def cal_fib_num(n):
    if n == 1:
        return 1
    a = 0
    b = 1
    c = 0
    for i in range(1, n):
        c = a + b
        a = b
        b = c
    return c
