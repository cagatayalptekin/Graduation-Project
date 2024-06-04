#https://leetcode.com/problems/search-insert-position/description/
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



# def find_insertion_index(arr, target):
#     # Initialize a binary search tree (BST) from the sorted array
#     root = Node(arr[0])
#     for i in range(1, len(arr)):
#         # If the current element is less than or equal to the target, move down the BST
#         if arr[i] <= target:
#             root.left = Node(arr[i])
#         else:
#             root.right = Node(arr[i])
#     # Perform a binary search for the target value in the BST
#     current = root
#     while current:
#         mid = (current.left + current.right) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             current = current.left
#         else:
#             current = current.right
    
#     # If we reached the end of the BST without finding the target, it means
#     # that the target is not in the array
#     if current == root:
#         return -1



def find_insertion_index(arr, target):
    n = len(arr)
    if target in arr:
        return arr.index(target)
    else:
        i = 0
        while i < n and arr[i] != target:
            i += 1
        if i == n:
            return -1 # Target not found, so return the index where it would be if it were inserted
        else:
            return i # Return the index of the insertion point
#diğer iki sonuçtada aynı cevabı verdi