#https://leetcode.com/problems/3sum/description/

# def get_triplets(nums):
#     triplets = []
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             for k in range(j+1, len(nums)):
#                 if nums[i] + nums[j] + nums[k] == 0:
#                     triplets.append([nums[i], nums[j], nums[k]])
#     return list(set(triplets))



def get_triplets(nums):
    # Initialize an empty list to store the result
    result = []
    # Sort the input array
    nums.sort()
    # Loop through the array and find the triplets
    for i in range(len(nums) - 2):
        j = i + 1
        k = len(nums) - 1
        while j < k:
            if nums[i] + nums[j] + nums[k] == 0:
                result.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
            else:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    k -= 1
    # Return the result
    return result