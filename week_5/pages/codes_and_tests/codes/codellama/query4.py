def checkPalindrome(num):
    str_num = str(num)
    isPalindrome = True

    for i in range(len(str_num)):
        if str_num[i] != str_num[-1 - i]:
            isPalindrome = False
            break

    return isPalindrome



