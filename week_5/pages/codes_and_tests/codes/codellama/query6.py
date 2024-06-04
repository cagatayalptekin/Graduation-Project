#Write a program that takes two strings as input and finds the longest substring that is common to both strings.
def longest_common_substring(str1, str2):
    m = len(str1)
    n = len(str2)
    dp = [[0 for x in range(n+1)] for y in range(m+1)]

    result = ""
    for i in range(m):
        for j in range(n):
            if str1[i] == str2[j]:
                dp[i+1][j+1] = dp[i][j] + 1
                if dp[i+1][j+1] > len(result):
                    result = str1[i-dp[i+1][j+1]+1:i+1]
            else:
                dp[i+1][j+1] = 0

    return result

