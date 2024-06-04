#https://leetcode.com/problems/two-sum/description/
#two sum 

def two_sum(nums, target):
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i




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

