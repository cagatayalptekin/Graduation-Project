# def armstrongNumber(n):
#     # Calculate the sum of the cubes of digits
#     total = 0
#     original_num = n
#     while n > 0:
#         digit = n % 10
#         total += digit ** 3
#         n //= 10

#     # Check if the sum of cubes is equal to the original number
#     return total == original_num

# def armstrongNumber(n):
#     # Calculate the sum of the cubes of digits
#     original = n
#     sum = 0
#     while n > 0:
#         digit = n % 10
#         sum += digit ** 3
#         n //= 10

#     # Check if the sum is equal to the original number
#     return sum == original

def armstrongNumber(num):
    """This function determines if the input number is an Armstrong number."""
    
    # Calculate the sum of cubes of digits
    original = num
    total = 0
    while num > 0:
        digit = num % 10
        total += (digit ** 3)
        num //= 10
        
    # Check if the sum of cubes equals the original number
    return total == original