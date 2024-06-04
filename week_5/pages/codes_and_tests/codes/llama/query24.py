#https://leetcode.com/problems/3sum-closest/description/

# def threeSumClosest(nums, target):
#     # Sort the array in ascending order
#     nums.sort()
    
#     # Initialize the closest sum to 0
#     closest_sum = 0
    
#     # Loop through the array and find the three integers that are closest to the target
#     for i in range(len(nums) - 2):
#         left = i + 1
#         right = len(nums) - 1
        
#         while left < right:
#             current_sum = nums[i] + nums[left] + nums[right]
#             if abs(target - current_sum) < abs(target - closest_sum):
#                 closest_sum = current_sum
            
#             if current_sum > target:
#                 right -= 1
#             else:
#                 left += 1
    
#     return closest_sum
import numpy as np


# def threeSumClosest(nums, target):
#     nums.sort()
#     closest = float("inf")
#     result = 0
#     for i in range(len(nums)-2):
#         l = i+1
#         r = len(nums)-1
#         while l < r:
#             curr_sum = nums[i] + nums[l] + nums[r]
#             if abs(curr_sum-target) < closest:
#                 closest = abs(curr_sum-target)
#                 result = curr_sum
#             if curr_sum > target:
#                 r -= 1
#             else:
#                 l += 1
#     return result

def threeSumClosest(nums, target):
    # Sort the array in ascending order to make it easier to find the closest sum
    nums.sort()
    
    # Calculate the difference between each element and the target value
    differences = [abs(x - target) for x in nums]
    
    # Find the three elements with the smallest differences
    closest_indices = np.argmin(differences, axis=0)
    
    # Return the sum of these three elements
    return nums[closest_indices]
