import math
#Given two positive integers left and right represented as strings, return the number of super-palindromes integers in the inclusive range [left, right].
def count_super_palindromes(left, right):
    # Convert the input strings to integers
    left = int(left)
    right = int(right)
    
    # Initialize a counter for the number of super-palindromes
    count = 0
    
    # Iterate over the range of integers from left to right
    for i in range(left, right+1):
        # Check if the integer is a palindrome
        if str(i) == str(i)[::-1]:
            # Check if the integer is the square of a palindrome
            for j in range(1, int(math.sqrt(i))+1):
                if pow(j, 2) == i:
                    count += 1
                    break
    
    return count