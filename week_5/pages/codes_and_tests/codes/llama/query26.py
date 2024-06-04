#https://leetcode.com/problems/median-of-two-sorted-arrays/description/

def find_median(nums1, nums2):
    m = len(nums1)
    n = len(nums2)
    if m < n: # handle the case where one array is shorter than the other
        return nums1[m // 2]
    else: # handle the case where both arrays are roughly equal in size
        midpoint = (m + n) // 2
        return (nums1[midpoint - m // 4] + nums1[midpoint + m // 4]) / 2.0




# def find_median(nums1, nums2):
#     # Check if the input arrays are empty
#     if not nums1 and not nums2:
#         return None

#     # Find the middle index of the two sorted arrays
#     mid1 = (len(nums1) - 1) // 2
#     mid2 = (len(nums2) - 1) // 2

#     # Calculate the median of the two sorted arrays
#     if len(nums1) + len(nums2) % 2 == 0:
#         return (max(nums1[mid1], nums2[mid2]) + min(nums1[mid1 + 1], nums2[mid2 + 1])) / 2
#     else:
#         return max(nums1[mid1], nums2[mid2])
    

#diger iki cevap çalıştılmadı