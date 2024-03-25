#query_2="Write a function that takes an integer as input and determines if it's a prime number"


def isPrime_codellama(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def is_prime_llama(n):
    """
    Checks if n is a prime number.

    Parameters:
        n (int) - The number to check for primality.

    Returns:
        bool - Whether n is a prime number or not.
    """
    # Base case: If n = 1, return False
    if n == 1:
        return False

    # Check if n is divisible by any of the prime numbers less than or equal to sqrt(n)
    for p in range(2, int(n ** 0.5)):
        if n % p == 0:
            return False

    # If we reach this point, n is likely to be a prime number
    return True
def is_prime_mistral(n):
    # check negative number
    if n < 0:
        return False
    # check 0 and 1
    elif n == 0 or n == 1:
        return False
    else:
        # check for factors up to the square root of n
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
