#https://leetcode.com/problems/integer-to-roman/description/
    
# def int_to_roman(number):
#     roman_numerals = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X",
#                      40: "XL", 50: "L", 90: "XC", 100: "C",
#                      400: "CD", 500: "D", 900: "CM", 1000: "M"}
#     roman_num = ""
#     i = 1000
#     while number > 0:
#         quotient = number // i
#         if quotient > 0:
#             roman_num += roman_numerals[i] * quotient
#             number -= i * quotient
#         i //= 10
#     return roman_num

def int_to_roman(num):
    # Define a dictionary for mapping numbers to Roman numerals
    roman = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X',
             40: 'XL', 50: 'L', 90: 'XC', 100: 'C',
             400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
    
    # Create an empty string to store the Roman numeral
    roman_num = ''

    # Loop through the number from right to left, adding the appropriate Roman numerals
    for key in reversed(list(roman.keys())):
        while num >= key:
            num -= key
            roman_num += roman[key]

    return roman_num

# def int_to_roman(number):
#     num_dict = {
#         1: 'I', 4: 'IV', 5: 'V', 9: 'IX',
#         10: 'X', 40: 'XL', 50: 'L', 90: 'XC',
#         100: 'C', 400: 'CD', 500: 'D', 900: 'CM',
#         1000: 'M'
#     }

#     roman_numeral = ''
#     for values in sorted(num_dict.items(), reverse=True):
#         while number >= values[0]:
#             roman_numeral += values[1]
#             number -= values[0]

#     return roman_numeral






