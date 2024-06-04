#https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
from collections import defaultdict

def longest_substring(s):
    if not s:
        return 0

    n = len(s)
    start = 0
    char_set = set()
    max_len = 0

    i = 0
    while i < n:
        if s[i] in char_set:
            start = max(start, i + 1)
        char_set.add(s[i])
        i += 1
        max_len = max(max_len, i - start)

    return max_len


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

#aynı sonuc verdi