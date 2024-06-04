#https://leetcode.com/problems/roman-to-integer/description/
#Given a roman numeral, convert it to an integer.

# def roman_to_int(roman_numeral):
#     roman_numeral_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
#     total = 0
#     for i in range(len(roman_numeral)):
#         if i > 0 and roman_numeral_map[roman_numeral[i]] > roman_numeral_map[roman_numeral[i-1]]:
#             total += roman_numeral_map[roman_numeral[i]] - 2 * roman_numeral_map[roman_numeral[i-1]]
#         else:
#             total += roman_numeral_map[roman_numeral[i]]
#     return total


def roman_to_int(roman):
    # Initialize variables for the conversion process
    int_value = 0
    num_digits = len(roman)
    
    # Iterate through each digit in the Roman numeral and convert it to an integer value
    for i in range(num_digits):
        if roman[i] == 'I':
            int_value += 1
        elif roman[i] == 'V':
            int_value += 5
        elif roman[i] == 'X':
            int_value += 10
        elif roman[i] == 'L':
            int_value += 50
        else:
            raise ValueError("Invalid Roman numeral")
    return int_value


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