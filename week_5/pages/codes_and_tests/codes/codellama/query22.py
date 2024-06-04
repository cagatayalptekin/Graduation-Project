#https://leetcode.com/problems/integer-to-roman/description/
    

def int_to_roman(number):
    num_dict = {
        1: 'I', 4: 'IV', 5: 'V', 9: 'IX',
        10: 'X', 40: 'XL', 50: 'L', 90: 'XC',
        100: 'C', 400: 'CD', 500: 'D', 900: 'CM',
        1000: 'M'
    }

    roman_numeral = ''
    for values in sorted(num_dict.items(), reverse=True):
        while number >= values[0]:
            roman_numeral += values[1]
            number -= values[0]

    return roman_numeral



