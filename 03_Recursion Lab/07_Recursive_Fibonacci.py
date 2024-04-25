number = int(input())


def calc_fib(number):
    if number <= 1:
        return 1
    return calc_fib(number - 1) + calc_fib(number - 2)


def iterative_fib(number):
    fib0 = 1
    fib1 = 1
    result = 0

    for _ in range(number - 1):
        result = fib0 + fib1
        fib0, fib1 = fib1, result
    return result


print(calc_fib(number))
print(iterative_fib(number))
