#query_4="Write a function that takes an integer as input and determines if it's a palindrome"



def checkPalindrome_codellama(num):
    str_num = str(num)
    isPalindrome = True

    for i in range(len(str_num)):
        if str_num[i] != str_num[-1 - i]:
            isPalindrome = False
            break

    return isPalindrome

def is_palindrome_llama(x):
    # Initialize a string with the given integer
    s = str(x)

    # Check if the string is empty
    if len(s) == 0:
        return True

    # If the string is not empty, check if it is a palindrome
    else:
        return s == s[::-1]

def is_palindrome_mistral(x):
    x = abs(x)
    s = str(x)
    return s == s[::-1]