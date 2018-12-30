def palindromeNumberSum(p_numDigits):

    """
    A palindromic number reads the same both ways. T
    he largest palindrome made from the product of two 2-digit numbers is:
    9009 = 91 × 99.

    Find the largest palindrome made from the product of two 3-digit numbers.
    :return:
    """
    nums = ['9']*p_numDigits
    str_max_nums = ''
    for i in nums:
        str_max_nums = str_max_nums + i

    max_nums = int(str_max_nums)
    num1 = max_nums
    num2 = max_nums
    num2_reduce = max_nums

    product = num1*num2

    while not reverse(str(product)):
        num2_reduce -= 1
        product = num1 * num2_reduce

    print('Number combo: {} * {} = {}'.format(num1, num2_reduce, product))


def reverse(p_str):
    """
    >>> reverse('123')
    False

    >>> reverse('909')
    True

    """
    r_str = ''
    for i, val in enumerate(p_str):
        r_str = p_str[i] + r_str

    return r_str == p_str

palindromeNumberSum(3)