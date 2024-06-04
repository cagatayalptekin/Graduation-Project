def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result


# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     mid = len(arr) // 2
#     left_half = arr[:mid]
#     right_half = arr[mid:]

#     merge_sort(left_half)
#     merge_sort(right_half)

#     i, j, result = 0, 0, []

#     while i < len(left_half) and j < len(right_half):
#         if left_half[i] < right_half[j]:
#             result.append(left_half[i])
#             i += 1
#         else:
#             result.append(right_half[j])
#             j += 1

#     result += left_half[i:]
#     result += right_half[j:]

#     arr = result
#     return arr


# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     mid = len(arr) // 2
#     left_half = arr[:mid]
#     right_half = arr[mid:]

#     merge_sort(left_half)
#     merge_sort(right_half)

#     i, j, k = 0, 0, 0

#     while i < len(left_half) and j < len(right_half):
#         if left_half[i] <= right_half[j]:
#             arr[k] = left_half[i]
#             i += 1
#         else:
#             arr[k] = right_half[j]
#             j += 1
#         k += 1

#     while i < len(left_half):
#         arr[k] = left_half[i]
#         i += 1
#         k += 1

#     while j < len(right_half):
#         arr[k] = right_half[j]
#         j += 1
#         k += 1

#     return arr