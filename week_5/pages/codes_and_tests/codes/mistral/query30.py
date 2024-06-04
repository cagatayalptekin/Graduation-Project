#https://leetcode.com/problems/trapping-rain-water/description/

def trapping_water(height):
    n = len(height)
    if not height or n <= 1:
        return 0

    left, right, result = 0, n-1, 0

    while left < right:
        # Find smaller height from both sides
        left_smaller = min(height[left], height[right])
        
        # Water capacity we can get at the current left index, will decrement with right's movements.
        water = left_smaller - height[left] if height[left] > left_smaller else 0
        
        result += water
        left += 1
        
        # Update right pointer to find next smaller height
        while height[right] >= left_smaller and right > left:
            right -= 1
            
    return result


# def trapping_water(heights):
#     # Find the maximum height
#     max_height = max(heights)

#     # Initialize the left and right pointers
#     left = 0
#     right = len(heights) - 1

#     # Initialize the total water trapped
#     total_water = 0

#     # Loop through the heights array
#     for i in range(len(heights)):
#         # If the current height is less than the maximum height, add it to the total water
#         if heights[i] < max_height:
#             total_water += (max_height - heights[i])

#     # Loop through the heights array in reverse order
#     for i in range(len(heights) - 1, -1, -1):
#         # If the current height is less than the maximum height, add it to the total water
#         if heights[i] < max_height:
#             total_water += (max_height - heights[i])

#     return total_water



#veya

#https://leetcode.com/problems/first-missing-positive/description/

def get_smallest_positive_integer_not_in_nums(nums):
    for i in range(1, len(nums)):
        if i not in nums:
            return i
    return len(nums) + 1