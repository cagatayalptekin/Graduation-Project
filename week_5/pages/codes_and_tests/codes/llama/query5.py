#def armstrongNumber(n):
#    return n ** 2 % 1 == 0  # Armstrong numbers have this property


def armstrongNumber(n):
    # Base case: check if n is 0 or 1
    if n == 0 or n == 1:
        return False
    
    # Check if n is a power of 2
    if n & (n - 1) == 0:
        return True
    
    # Recursively check if n is an Armstrong number
    for i in range(2, int(n ** 0.5) + 1):
        if armstrongNumber(n // i):
            return True
    
    return False



