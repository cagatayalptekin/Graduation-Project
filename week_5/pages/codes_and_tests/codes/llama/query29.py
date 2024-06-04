#https://leetcode.com/problems/search-in-rotated-sorted-array/description/
def search_number_in_rotated_sorted_array(arr, target):
    # Initialize the left and right indices
    left = 0
    right = len(arr) - 1

    # While the number is not found
    while left <= right:
        # Calculate the middle index
        mid = (left + right) // 2

        # If the number is found at the middle index, return it
        if arr[mid] == target:
            return mid

        # If the number is less than the middle index, move to the right
        elif arr[mid] < target:
            right = mid - 1
        else:
            left = mid + 1
    return None

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


