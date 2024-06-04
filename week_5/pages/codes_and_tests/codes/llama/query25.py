#https://leetcode.com/problems/jump-game/description/

# def can_reach_end(nums):
#     # Initialize variables
#     current = 0
#     max_jump = nums[current]
#     while current < len(nums) - 1:
#         # Calculate the next jump length based on the current maximum jump length and the distance between current and next indices
#         next_jump = min(max_jump, len(nums[current+1]) - current)
#         # Check if we can reach the end of the array
#         if current + next_jump == len(nums):
#             return True
#         # Update the maximum jump length for the next iteration
#         max_jump = min(max_jump, next_jump)
#         # Move to the next index and repeat the process
#         current += 1
#     return False



def can_reach_end(nums):
    # Initialize a list to keep track of the maximum jump length at each position
    max_jumps = [0] * len(nums)
    # Start at the first index and iterate through the array
    for i in range(1, len(nums)):
        # Get the current element's value
        current = nums[i]
        # If we can jump from the previous position to this position, add the maximum jump length to our list
        if current - max_jumps[-1] > 0:
            max_jumps.append(current)
            # Otherwise, move on to the next element and repeat the process
        else:
            break
    return len(max_jumps) == len(nums)




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