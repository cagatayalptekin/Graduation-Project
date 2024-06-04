#https://leetcode.com/problems/3sum/description/

# def get_triplets(nums):
#     triplets = []
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             for k in range(j+1, len(nums)):
#                 if nums[i] + nums[j] + nums[k] == 0:
#                     triplets.append([nums[i], nums[j], nums[k]])
#     return list(set(triplets))



# def get_triplets(nums):
#     # Initialize an empty list to store the result
#     result = []
#     # Sort the input array
#     nums.sort()
#     # Loop through the array and find the triplets
#     for i in range(len(nums) - 2):
#         j = i + 1
#         k = len(nums) - 1
#         while j < k:
#             if nums[i] + nums[j] + nums[k] == 0:
#                 result.append([nums[i], nums[j], nums[k]])
#                 j += 1
#                 k -= 1
#             else:
#                 if nums[i] + nums[j] + nums[k] < 0:
#                     j += 1
#                 else:
#                     k -= 1
#     # Return the result
#     return result


# def get_triplets(nums):
#     # Create a dictionary to keep track of visited indices
#     visited = set()

#     # Iterate over the array and find all possible triplets
#     for i in range(len(nums)):
#         if i not in visited:
#             # Check if current index is equal to any of the other two indices
#             for j in range(i+1, len(nums)):
#                 if j not in visited and nums[j] + nums[i] == 0:
#                     # Add the triplet to the list
#                     yield (nums[i], nums[j], nums[k])
#             # Mark the current index as visited
#             visited.add(i)
#     # Return an empty list if no triplets were found
#     return []


def get_triplets(nums):
    # Create a dictionary to store the triplets
    result = {}
    
    # Loop through all elements in the array
    for i in range(len(nums)):
        # If this element is not already in the list of triplets, add it
        if nums[i] not in result:
            # Find all pairs that sum to 0 with this element
            for j in range(i+1, len(nums)):
                if nums[j] + nums[i] == 0:
                    # Add the triplet to the list of results
                    result.add((nums[i], nums[j], nums[k]))
    return result