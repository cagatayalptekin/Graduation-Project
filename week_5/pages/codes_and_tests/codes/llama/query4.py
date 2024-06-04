def checkPalindrome(x):
    # Initialize a string with the given integer
    s = str(x)

    # Check if the string is empty
    if len(s) == 0:
        return True

    # If the string is not empty, check if it is a palindrome
    else:
        return s == s[::-1]