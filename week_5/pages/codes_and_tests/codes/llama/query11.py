def second_largest(numbers):
    # Initialize the current largest element as -1
    largest = -1
    # Iterate through the array and keep track of the current largest element
    for i in range(len(numbers)):
        if numbers[i] > largest:
            largest = numbers[i]
    # Return the second largest element
    return largest

# def second_largest(arr):
#     # Initialize two variables to store the current second largest element and its index
#     current_second_largest = arr[0]
#     current_index = 0
    
#     # Loop through the array, keeping track of the current second largest element and its index
#     for i in range(1, len(arr)):
#         if arr[i] > current_second_largest:
#             current_second_largest = arr[i]
#             current_index = i
    
#     # Return the second largest element and its index
#     return current_second_largest, current_index

# def second_largest(arr):
#     # Set a variable to keep track of the current candidate for the second largest number
#     second_largest = arr[0]
    
#     # Loop through the array and check if any element is larger than the current candidate
#     for i in range(1, len(arr)):
#         if arr[i] > second_largest:
#             second_largest = arr[i]
    
#     return second_largest