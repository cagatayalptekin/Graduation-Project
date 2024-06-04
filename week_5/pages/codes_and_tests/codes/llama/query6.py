def longest_common_substring(str1, str2):
    # Create a dictionary to store the longest common substrings
    longest_common_dict = {}
    
    # Loop through the characters of both strings and find the longest common substring
    for char1 in str1:
        for char2 in str2:
            if char1 == char2:
                # If we find a match, add it to the dictionary
                if char1 not in longest_common_dict:
                    longest_common_dict[char1] = 1
                else:
                    longest_common_dict[char1] += 1
    
    # Return the longest common substring
    return max(longest_common_dict.keys())

# def longest_common_substring(str1, str2):
#     # Initialize two empty lists to store the characters of the strings
#     char1 = []
#     char2 = []

#     # Loop through each character of the first string
#     for c in str1:
#         # If the character is not in the second string, add it to the list of unique characters of the first string
#         if c not in char2:
#             char1.append(c)
#             char2.append(c)
        
#     # Find the longest common substring by finding the longest sequence of consecutive characters that are in both lists
#     longest_common_substring = max(len(char1), len(char2))
#     return longest_common_substring