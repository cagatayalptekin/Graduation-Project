#https://leetcode.com/problems/two-sum/description/
#two sum 


# def two_sum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]
#     return []

# def two_sum(nums, target):
#     seen = {}
#     for i, num in enumerate(nums):
#         if num in seen:
#             return [seen[num], i]
#         else:
#             seen[target - num] = i
#     return []

def two_sum(nums, target):
    # Sort the array of integers to make it easier to search for the correct indices
    nums = sorted(nums)
    # Initialize two variables to keep track of the indices of the numbers that add up to the target
    left = 0
    right = len(nums) - 1
    while left < right:
        sum = nums[left] + nums[right]
        if sum == target:
            return [left, right] # Found a solution, return the indices of the numbers that add up to the target
        elif sum > target:
            right -= 1 # Move right index to the next number in the array
        else:
            left += 1 # Move left index to the previous number in the array
    # If we reach this point, there is no solution for the given input
    return []


#diğer secenek hepsi hata verdi





# def two_sum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]
#     return []


# def two_sum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]
#     return []

