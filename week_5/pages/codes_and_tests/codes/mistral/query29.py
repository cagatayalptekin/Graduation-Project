#https://leetcode.com/problems/search-in-rotated-sorted-array/description/

def search_number_in_rotated_sorted_array(arr, target):
    # Define the left and right pointers
    low = 0
    high = len(arr) - 1
    
    # Continue searching while the pointers are within the bounds of the array
    while low <= high:
        mid = (low + high) // 2  # Calculate the middle index
        
        # If the middle element matches the target, return its index
        if arr[mid] == target:
            return mid

        # Update pointers based on comparison of target and current middle element
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    # If the target is not found, return -1
    return -1
# def search_number_in_rotated_sorted_array(arr, target):
#     left = 0
#     right = len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[left] <= arr[mid]:
#             # If the left half is sorted, then the target must be in the right half
#             if arr[left] <= target < arr[mid]:
#                 right = mid - 1
#             else:
#                 left = mid + 1
#         else:
#             # If the right half is sorted, then the target must be in the left half
#             if arr[mid] < target <= arr[right]:
#                 left = mid + 1
#             else:
#                 right = mid - 1
#     return -1


# def search_rotated_sorted_array(arr, target):
#     left = 0
#     right = len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1


