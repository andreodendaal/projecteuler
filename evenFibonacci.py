def evenFibonacci(p_target):
    """
    0 + 1 = 1
    1 + 1 = 2

    :param p_range:
    :return:
    """
    fib_values = []
    fib_values_even = []
    fib_values.append(0)
    fib_values.append(1)
    i = 0
    while fib_values[i] < p_target:
    #for i in range(p_range):
        #print(i)
        fib_values.append(fib_values[i+1] + fib_values[i])
        if fib_values[i] % 2 == 0:
            fib_values_even.append(fib_values[i])

        i += 1

        #print(fib_values)
    #print(fib_values)
    #print(fib_values_even)
    return sum(fib_values_even)

print(evenFibonacci(4000000))