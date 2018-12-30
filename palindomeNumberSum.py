def palindromeNumberSum(p_numDigits):

    """
    A palindromic number reads the same both ways. T
    he largest palindrome made from the product of two 2-digit numbers is:
    9009 = 91 × 99.

    Find the largest palindrome made from the product of two 3-digit numbers.

    >>> palindromeNumberSum(3)
    906609

    >>> palindromeNumberSum(2)
    9009
    :return:
    """
    nums = ['9']*p_numDigits
    str_max_nums = ''
    for i in nums:
        str_max_nums = str_max_nums + i

    max_nums = int(str_max_nums)
    num2_reduce = max_nums
    num1_reduce = max_nums
    product_max = 0

    while num1_reduce > 0:

        while num2_reduce > 0:
            # For each first product number run through the entire range of the
            # 2nd product options
            product = num1_reduce * num2_reduce
            if reverse(str(product)):
                # Save the largest resultant palindrome and the two products
                if product > product_max:
                    product_max = product
                    num1_max = num1_reduce
                    num2_max = num2_reduce
            num2_reduce -= 1

        num1_reduce -= 1
        num2_reduce = max_nums

    print(str(product_max))
    print('Number combo: {} * {} = {}'.format(num1_max, num2_max, product_max))


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