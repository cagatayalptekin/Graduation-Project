def armstrongNumber(n):
    # Initialize variables
    cubed_digits = []
    for digit in str(n):
        cubed_digits.append(int(digit ** 3))
    sum_of_cubes = sum(cubed_digits)
    
    # Check if the sum of the cube of the digits is equal to the original number
    return sum_of_cubes == n

# def is_armstrong(n):
#     # Convert n to a string of digits
#     num = str(n)
    
#     # Calculate the sum of the cube of the digits
#     cubes = [int(x**3) for x in num]
#     total = reduce(lambda x, y: x + y, cubes)
    
#     # Check if the total is equal to n
#     return total == n