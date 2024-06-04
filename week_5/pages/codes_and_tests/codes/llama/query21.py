#https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

# def longest_substring(s):
#     start = 0
#     max_length = 0
#     char_map = {}
#     for i in range(len(s)):
#         if s[i] in char_map and start <= char_map[s[i]]:
#             start = char_map[s[i]] + 1
#         else:
#             max_length = max(max_length, i - start + 1)
#         char_map[s[i]] = i
#     return max_length

# def longest_substring(s):
#     # Initialize two empty lists: longest_length and current_position
#     longest_length = []
#     current_position = 0
    
#     # Loop through the string s, keeping track of the current position and the longest substring length
#     for i in range(len(s)):
#         # If we reach the end of the string without finding a repeating character, add the current position to the list of longest lengths
#         if i == len(s) - 1:
#             longest_length.append(current_position)
        
#         # Otherwise, keep track of the current position and continue looping
#         else:
#             current_position += 1
    
#     return max(longest_length, key=len)

def longest_substring(s):
    # Initialize two dictionaries d and count to keep track of the lengths and counts of substrings
    d = {}
    count = 0
    for char in s:
        if char not in d:
            d[char] = 1
            count += 1
        else:
            d[char] += 1
    
    # Return the length of the longest substring without repeating characters
    return max(count, key=d.get)

#aynı sonuc verdi