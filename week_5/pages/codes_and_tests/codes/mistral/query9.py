def rotate_array(nums, k):
    # Calculate the number of positions to be moved from the end
    k = k % len(nums)
    
    # Shift the array by the calculated number of positions
    first_part = nums[-k:]
    nums[-k:] = []
    last_part = nums[:len(nums)-k]
    nums[:len(nums)-k] = first_part
    
    return nums

# def rotate_array(arr, rotate_by):
#     """Rotates arr by 'rotate_by' positions in place"""

#     # Find the length of the array
#     n = len(arr)

#     # Rotate arr by 'rotate_by' positions
#     arr[0:n-rotate_by] += rotate_by
#     arr[n-rotate_by:] = arr[0:n-rotate_by][::-1]