def isPrime(n):
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