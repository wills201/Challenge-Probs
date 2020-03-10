def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
        


def fib2(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    fib_list = [i for i in range(n)]
    fib_1 = fib_list[n-1]
    fib_2 = fib_list[n-2]
    actual_fib = fib_1 + fib_2
    return actual_fib
print(fib2(5))