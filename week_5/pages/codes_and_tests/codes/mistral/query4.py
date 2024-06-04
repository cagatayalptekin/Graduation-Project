def checkPalindrome(x):
    x = abs(x)
    s = str(x)
    return s == s[::-1]