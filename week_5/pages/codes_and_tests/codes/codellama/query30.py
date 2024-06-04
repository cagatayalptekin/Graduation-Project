#https://leetcode.com/problems/trapping-rain-water/description/

def trapping_water(heights):
    # Find the maximum height
    max_height = max(heights)

    # Initialize the left and right pointers
    left = 0
    right = len(heights) - 1

    # Initialize the total water trapped
    total_water = 0

    # Loop through the heights array
    for i in range(len(heights)):
        # If the current height is less than the maximum height, add it to the total water
        if heights[i] < max_height:
            total_water += (max_height - heights[i])

    # Loop through the heights array in reverse order
    for i in range(len(heights) - 1, -1, -1):
        # If the current height is less than the maximum height, add it to the total water
        if heights[i] < max_height:
            total_water += (max_height - heights[i])

    return total_water



#veya

#https://leetcode.com/problems/first-missing-positive/description/

def get_smallest_positive_integer_not_in_nums(nums):
    for i in range(1, len(nums)):
        if i not in nums:
            return i
    return len(nums) + 1