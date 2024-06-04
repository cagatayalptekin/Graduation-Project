#Write a program that takes an integer as input and determines if it's an Armstrong number (a number whose sum of the cube of its digits is equal to the original number, e.g., 153)

# def armstrongNumber(n):
#     num_of_digits = len(str(n))
#     sum = 0
#     for digit in str(n):
#         sum += int(digit) ** num_of_digits
#     if sum == n:
#         return "true"
#     else:
#         return "false"


# def armstrongNumber(num):
#     # Determine the number of digits in the input number
#     num_digits = len(str(num))

#     # Calculate the sum of each digit raised to the power of the number of digits
#     sum = 0
#     for digit in str(num):
#         sum += int(digit) ** num_digits

#     # Check if the input number is equal to the calculated sum
#     return sum == num

def armstrongNumber(n):
    # Calculate the sum of the cubes of each digit
    digits = [int(d) for d in str(n)]
    cube_sum = sum([pow(digit, 3) for digit in digits])
    # Check if the input number is equal to the calculated sum
    return n == cube_sum