#https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

def longest_substring(s):
    start = 0
    max_length = 0
    char_map = {}
    for i in range(len(s)):
        if s[i] in char_map and start <= char_map[s[i]]:
            start = char_map[s[i]] + 1
        else:
            max_length = max(max_length, i - start + 1)
        char_map[s[i]] = i
    return max_length

#aynı sonuc verdi