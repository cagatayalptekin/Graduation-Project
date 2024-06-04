#https://leetcode.com/problems/jump-game/description/

def can_reach_end(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    current_index = 0
    max_reachable = 0
    for index in enumerate(nums):
        # If we cannot reach the current position, return False
        if current_index >= len(nums) - 1:
            return True
        max_reachable = max(max_reachable, current_index + index[1])
        # If we cannot reach any further, return False
        if max_reachable <= current_index:
            return False
        current_index += 1
    return True

# def can_reach_end(nums):
#     # Initialize the current position as the first index of the array
#     current = 0
#     # Loop through the array
#     for i in range(len(nums)):
#         # Check if the current position is greater than or equal to the maximum jump length at the current position
#         if current >= len(nums) - 1:
#             # If it is, return true
#             return True
#         # Check if the current position plus the maximum jump length at the current position is greater than or equal to the last index of the array
#         if current + nums[i] >= len(nums) - 1:
#             # If it is, set the current position to the last index of the array
#             current = len(nums) - 1
#     # If you reach the end of the array, return true
#     return True


# def can_reach_end(nums):
#     n = len(nums)
#     if n == 0:
#         return False
#     elif n == 1:
#         return True
#     else:
#         for i in range(n-1):
#             if nums[i] >= i+1 and can_reach_end(nums[:i] + nums[i+1:]):
#                 return True
#         return False
    
# def can_reach_end(nums):
#     current = 0
#     n = len(nums) - 1
#     while current <= n:
#         prev = current
#         current = max(current + nums[current], current)
#         if current == n:
#             return True
#         if current < prev:
#             return False
#     return False