
def primeFactors(p_number):
    """
    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?

    """


    # Initialize a list
    primes = []
    prime_sum = 1

    while prime_sum < p_number:

        for possiblePrime in range(2, p_number + 1):
            # Assume number is prime until shown it is not.
            isPrime = True
            for num in range(2, possiblePrime):
                if possiblePrime % num == 0:
                    isPrime = False
            if isPrime:
                primes.append(possiblePrime)
                prime_sum = prime_sum * possiblePrime

    return prime_sum

def primefactors2(n):

    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            print('n before: {}'.format(n))
            print(i)
            n //= i
            print('n after: {}'.format(n))
    return n

p = 13195
print(primefactors2(p))