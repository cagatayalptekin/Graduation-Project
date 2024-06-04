# def longest_common_substring(str1, str2):
#     m = len(str1)
#     n = len(str2)

#     # Create a table to store lengths of longest common suffixes of substrings
#     dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

#     max_length = 0
#     index = 0

#     # Fill the table from bottom up manner
#     for i in range(m + 1):
#         for j in range(n + 1):
#             if i == 0 or j == 0:
#                 dp[i][j] = 0
#             elif str1[i - 1] == str2[j - 1]:
#                 dp[i][j] = dp[i - 1][j - 1] + 1
#                 if dp[i][j] > max_length:
#                     max_length = dp[i][j]
#                     index = i - 1
#             else:
#                 dp[i][j] = 0

#     # Return the longest common substring
#     return str1[index:index + max_length]


def longest_common_substring(str1, str2):
    m = len(str1)
    n = len(str2)

    # Create a table to store lengths of longest common suffixes of substrings
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    max_length = 0
    index = 0

    # Fill the table from bottom up manner
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    index = i - 1
            else:
                dp[i][j] = 0

    # Return the longest common substring
    return str1[index - max_length + 1 : index + 1]