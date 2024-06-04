#https://leetcode.com/problems/container-with-most-water/description/

def max_water(height):
    # Find the index of the maximum element in the array
    max_index = height.index(max(height))

    # Initialize the maximum area variable
    max_area = 0

    # Loop through the indices of the array and find the maximum area between two lines
    for i in range(max_index):
        for j in range(i+1, max_index):
            width = j - i
            height = min(height[i], height[j])
            area = width * height
            if area > max_area:
                max_area = area

    return max_area


#diger cevaplar çalıştılımadı