#https://leetcode.com/problems/container-with-most-water/description/

# def max_water(height):
#     left, right = 0, len(height) - 1
#     max_area = 0
#     while left < right:
#         curr_area = min(height[left], height[right]) * (right-left)
#         if curr_area > max_area:
#             max_area = curr_area

#         # move pointer towards the direction having smaller height to increase the area
#         if height[left] < height[right]:
#             left += 1
#         else:
#             right -= 1
#     # when pointers meet, check for the last line
#     if left == right:
#         max_area = height[left]

#     return max_area

def max_water(height):
    # Initialize variables for left and right pointers, and maximum water capacity
    left = 0
    right = len(height) - 1
    max_capacity = 0

    # Two pointers approach with width as current minimum height between the two pointers
    while left < right:
        min_height = min(height[left], height[right])
        width = right - left
        capacity = min_height * width
        max_capacity = max(max_capacity, capacity)
        if height[left] < min_height:
            left += 1
        else:
            right -= 1

    return max_capacity


# def max_water(height):
#     # Find the index of the maximum element in the array
#     max_index = height.index(max(height))

#     # Initialize the maximum area variable
#     max_area = 0

#     # Loop through the indices of the array and find the maximum area between two lines
#     for i in range(max_index):
#         for j in range(i+1, max_index):
#             width = j - i
#             height = min(height[i], height[j])
#             area = width * height
#             if area > max_area:
#                 max_area = area

#     return max_area


#diger cevaplar çalıştılımadı