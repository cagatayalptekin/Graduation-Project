# def rotate_array(arr, num_positions):
#     # Handle edge cases
#     if num_positions == 0:
#         return arr
#     elif num_positions < 0:
#         raise ValueError("Negative number of positions")
#     # Calculate the new starting index
#     new_start = (arr.shape[0] - num_positions) % arr.shape[1]
#     # Rotate the array
#     return arr[new_start:]

# def rotate_array(arr, num_positions):
#     # Handle edge cases
#     if num_positions == 0:
#         return arr
#     elif num_positions < 0:
#         raise ValueError("Negative number of positions")
    
#     # Calculate the new starting index
#     new_start = (arr.shape[0] - num_positions) % arr.shape[1]
    
#     # Rotate the array
#     return arr[new_start:new_start+arr.shape[1]]


def rotate_array(arr, num_positions):
    # Create a new array with the same size as the original arr
    new_arr = []
    for i in range(len(arr)):
        # If the current element is past the rotation point, shift it to the left
        if i >= num_positions:
            new_arr.append(arr[i - num_positions])
        # Otherwise, just append the original element
        else:
            new_arr.append(arr[i])
    return new_arr