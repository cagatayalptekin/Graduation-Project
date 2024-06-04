def isPrime(n):
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