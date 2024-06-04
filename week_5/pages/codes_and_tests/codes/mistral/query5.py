# def armstrongNumber(n):
#     n_str = str(n)
#     sum_cubes = sum([int(digit)**3 for digit in n_str])
#     return n == sum_cubes

def armstrongNumber(n):
    # Get the number of digits in n
    num_digits = len(str(abs(n)))
    
    # Calculate sum of each digit raised to power 'num_digits' and check if it equals n
    total = 0
    original_number = abs(n)
    while original_number > 0:
        digit = original_number % 10
        total += digit ** num_digits
        original_number //= 10
    
    if total == n:
        return True
    else:
        return False