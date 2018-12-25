

def multiples_3_5(p_range):
    """
    >>> multiples_3_5(10)
    23
    """
    sum_range = 0
    for i in range(p_range):
        if i % 3 == 0 or i % 5 == 0:
            sum_range += i

    return sum_range

print(multiples_3_5(1000))