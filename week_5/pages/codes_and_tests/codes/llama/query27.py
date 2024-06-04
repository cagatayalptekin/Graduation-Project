#https://leetcode.com/problems/container-with-most-water/description/

def max_water(height):
    n = len(height)
    # Create a dictionary to keep track of the maximum area for each line
    areas = {i: 0 for i in range(n)}
    # Iterate over all possible pairs of lines and calculate their area
    for i in range(n-1):
        j = (i+1) % n
        area = height[i] + height[j] - height[(i+1)%n]
        areas[i] += area
    # Return the maximum area of any container
    return max(areas.values())
# Example usage:


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