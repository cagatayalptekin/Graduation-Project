#https://leetcode.com/problems/integer-to-roman/description/
    

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


def int_to_roman(n):
  # Use a mapping from integers to Roman numerals to make the conversion
  romans = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
  }
  # If the input is negative, adjust it so that it becomes positive
  if n < 0:
    n = abs(n)
  
  # Otherwise, simply convert the integer to a Roman numeral
  roman_str = romans[str(n)] + ""
  return roman_str





