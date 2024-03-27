#query_6="Write a program that takes two strings as input and finds the longest substring that is common to both strings."

def longest_common_substring_codellama(s1, s2):
    m = len(s1)
    n = len(s2)
    dp = [[0 for x in range(n+1)] for y in range(m+1)]
    result = ""
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j]

def find_longest_common_substring_llama(str1, str2):
    # Create a dictionary to store the characters of the first string
    char_dict = {}
    for i in range(len(str1)):
        char_dict[str1[i]] = 1

    # Create a dictionary to store the characters of the second string
    char_dict2 = {}
    for j in range(len(str2)):
        char_dict2[str2[j]] = 1

    # Find the longest common substring by iterating through the characters of both strings
    longest_common_substring = ""
    for i in range(len(char_dict)):
        if char_dict[i] and char_dict2[i]:
            longest_common_substring += str(i)
    return longest_common_substring

def longest_common_substring_mistral(s1, s2):
    m = len(s1)
    n = len(s2)
    maxLength = 0
    start = 0
    for i in range(m+1):
        for j in range(n+1):
            if i > 0 and j > 0 and s1[i-1] == s2[j-1]:
                k = i - 1
                l = j - 1
                while k >= 0 and l >= 0 and s1[k] == s2[l]:
                    if (l - j + 1) > maxLength:
                        start = i - 1
                        maxLength = l - j + 1
                    k -= 1
                    l -= 1
            else:
                i -= 1
                j -= 1
    return s1[start:start+maxLength]