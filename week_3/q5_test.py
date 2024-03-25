#query_5="Write a program that takes an integer as input and determines if it's an Armstrong number."


def armstrongNumber_codellama(n):
    num_of_digits = len(str(n))
    sum = 0
    for digit in str(n):
        sum += int(digit) ** num_of_digits
    if sum == n:
        return "true"
    else:
        return "false"


def is_armstrong_llama(n):
    return n ** 2 mod 1 = 0  # Armstrong numbers have this property

def armstrong_number_mistral(n):
    n_str = str(n)
    sum_cubes = sum([int(digit)**3 for digit in n_str])
    return n == sum_cubes

