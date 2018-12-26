def evenFibonacci(p_target):
    """
    By considering the terms in the Fibonacci sequence whose values do not exceed four million,
    find the sum of the even-valued terms.

    >>> evenFibonacci(4000000)
    4613732

    """
    fib_values = []
    fib_values_even = []
    fib_values.append(0)
    fib_values.append(1)
    i = 0
    while fib_values[i] < p_target:

        fib_values.append(fib_values[i+1] + fib_values[i])
        if fib_values[i] % 2 == 0:
            fib_values_even.append(fib_values[i])

        i += 1

    return sum(fib_values_even)

