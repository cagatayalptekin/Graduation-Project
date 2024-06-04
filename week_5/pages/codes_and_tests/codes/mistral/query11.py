def second_largest(arr):
    # Initialize first and second largest with first two elements of the array
    if len(arr) < 2:
        return None
    first_largest = arr[0]
    second_largest = arr[1]

    # Iterate through the array to find the second largest number
    for num in arr[1:]:
        if num > first_largest:
            second_largest, first_largest = first_largest, num
        elif num > second_largest and num != first_largest:
            second_largest = num

    return second_largest


# def second_largest(input_list):
#     # Check if there are at least two elements in the list
#     if len(input_list) < 2:
#         raise ValueError("The list should have at least two elements")

#     max1 = float('-inf')
#     max2 = float('-inf')

#     for num in input_list:
#         if num > max1:
#             # If new number is larger than current largest, replace it
#             max2 = max1
#             max1 = num
#         elif num > max2 and num != max1:
#             # If new number is larger than current second largest, update it
#             max2 = num

#     return max2


# def find_second_largest(arr):
#     if len(arr) < 2:
#         raise ValueError("Array should have at least 2 elements")
#     max_num = float('-inf')
#     sec_max_num = float('-inf') # Initialize both to the smallest possible value of a number
     
#     for num in arr:
#         if num > max_num:
#             sec_max_num = max_num  # If new number is larger than current second largest, old one becomes second
#             max_num = num
#         elif num > sec_max_num and num != max_num:
#             sec_max_num = num   # Update the second largest if it's smaller but not equal to the maximum
#     return sec_max_num
