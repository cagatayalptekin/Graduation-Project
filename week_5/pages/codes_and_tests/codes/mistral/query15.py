def reverse(num):
    """
    Helper function to reverse a number.
    """
    rev = 0
    while num > 0:
        digit = num % 10
        rev = (rev * 10) + digit
        num //= 10
    return rev

def is_superpalindrome(num, str_num):
    """
    Check if a number is super-palindrome.
    """
    binary = bin(num)[2:].zfill(len(bin(int(str_num[::-1])[2:])) * 2)
    return num == int(binary, 2) or int(str_num[::-1], 10) == reversed(num)

def count_super_palindromes(left, right):
    """
    Function to find the count of super-palindromes between two given positive integers.
    """
    count = 0
    for num in range(int(left), int(right) + 1):
        if is_superpalindrome(num, str(num)):
            count += 1
    return count