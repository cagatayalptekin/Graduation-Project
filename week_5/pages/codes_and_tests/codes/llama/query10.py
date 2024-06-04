# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     else:
#         mid = len(arr) // 2
#         left = arr[:mid]
#         right = arr[mid:]
#         merged = merge(left, right)
#         return merged

# def merge(left, right):
#     result = []
#     while len(left) > 0 and len(right) > 0:
#         if left[0] <= right[0]:
#             result.append(left.pop(0))
#         else:
#             result.append(right.pop(0))
#     return result


# def merge_sort(arr):
#     # Base case: If the length of the array is 1 or less, return it directly
#     if len(arr) <= 1:
#         return arr

#     # Split the array into two halves
#     mid = len(arr) // 2
#     left = arr[:mid]
#     right = arr[mid:]

#     # Recursively sort the left and right halves
#     left_sorted = merge_sort(left)
#     right_sorted = merge_sort(right)

#     # Merge the sorted left and right halves into a single sorted array
#     merged = merge(left_sorted, right_sorted)

#     return merged


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merged = merge(left, right)
        return merged

def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    return result