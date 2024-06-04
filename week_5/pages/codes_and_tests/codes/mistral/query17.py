#https://leetcode.com/problems/roman-to-integer/description/
#Given a roman numeral, convert it to an integer.


ROMAN_NUMERALS = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

def roman_to_int(roman):
    int_val = 0
    prev_val = 0
    for char in roman[::-1]:
        current_val = ROMAN_NUMERALS[char]
        if prev_val and current_val > prev_val:
            int_val += (current_val - (2 * prev_val))
        else:
            int_val += current_val
        prev_val = current_val
    return int_val

# def roman_to_int(roman_numeral):
#     roman_numeral_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
#     total = 0
#     for i in range(len(roman_numeral)):
#         if i > 0 and roman_numeral_map[roman_numeral[i]] > roman_numeral_map[roman_numeral[i-1]]:
#             total += roman_numeral_map[roman_numeral[i]] - 2 * roman_numeral_map[roman_numeral[i-1]]
#         else:
#             total += roman_numeral_map[roman_numeral[i]]
#     return total


# def roman_to_int(roman_numeral):
#     roman_numeral_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
#     total = 0
#     for i in range(len(roman_numeral)):
#         if i > 0 and roman_numeral_map[roman_numeral[i]] > roman_numeral_map[roman_numeral[i-1]]:
#             total += roman_numeral_map[roman_numeral[i]] - 2 * roman_numeral_map[roman_numeral[i-1]]
#         else:
#             total += roman_numeral_map[roman_numeral[i]]
#     return total


# def roman_to_int(roman_numeral):
#     roman_numeral_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
#     total = 0
#     for i in range(len(roman_numeral)):
#         if i > 0 and roman_numeral_map[roman_numeral[i]] > roman_numeral_map[roman_numeral[i-1]]:
#             total += roman_numeral_map[roman_numeral[i]] - 2 * roman_numeral_map[roman_numeral[i-1]]
#         else:
#             total += roman_numeral_map[roman_numeral[i]]
#     return total