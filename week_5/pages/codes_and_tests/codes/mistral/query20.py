#https://leetcode.com/problems/search-insert-position/description/

def find_insertion_index(arr, target):
    left = 0
    right = len(arr) - 1
    
    # Continue searching while the range is not empty
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    # If we reach here, then the target is not present in the array
    return left


# def find_insertion_index(arr, target):
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
    
#     return left


#diğer iki sonuçtada aynı cevabı verdi