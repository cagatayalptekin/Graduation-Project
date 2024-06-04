# def count_super_palindromes(left, right):
#     # Convert the strings to integers
#     left = int(left)
#     right = int(right)

#     # Calculate the number of super-palindromes in the inclusive range
#     count = 0
#     for i in range(left, right+1):
#         if i == i[::-1]:
#             count += 1
#     return count

# def count_super_palindromes(left, right):
#     # Initialize a dictionary to store the counts
#     counts = {0: 1}

#     # Loop through the range [left, right] and count the number of super-palindromes
#     for i in range(left, right + 1):
#         # Check if the number is a super-palindrome
#         if check_super_palindrome(i):
#             # Increment the count
#             counts[i] = counts.get(i, 0) + 1
#     return counts

# # Define a function to check if a number is a super-palindrome
# def check_super_palindrome(n):
#     # Split the number into its digits
#     digits = str(n).split()
#     # Check if the number is palindromic
#     if digits[0] == digits[-1]:
#         # Check if the number is positive
#         if n > 0:
#             # Return True if it's a super-palindrome, False otherwise
#             return True


def count_super_palindromes(left, right):
    # Convert both numbers to digits and sort them
    left_digits = list(map(str, left))
    right_digits = list(map(str, right))
    sorted_left = sorted(left_digits)
    sorted_right = sorted(right_digits)
    
    # Keep track of the number of super-palindromes found so far
    count = 0
    # Loop through the sorted digits and check if they form a super-palindrome
    for i in range(len(sorted_left)):
        current = sorted_left[i]
        remaining = [x for x in sorted_right if x != current]
        if len(remaining) == 0:
            # This is a super-palindrome! Count it and break out of the loop
            count += 1
        else:
            # Not a super-palindrome, move on to the next digit
            continue
    return count