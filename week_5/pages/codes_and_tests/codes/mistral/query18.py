#https://leetcode.com/problems/longest-common-prefix/description/
# def longest_common_prefix(strs):
#     if not strs:
#         return ""
#     shortest_str = min(strs, key=len)
#     for i, c in enumerate(shortest_str):
#         for str in strs:
#             if len(str) <= i or c != str[i]:
#                 return shortest_str[:i]
#     return shortest_str


#https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
#remove duplicates from sorted array

def remove_duplicates(arr):
    """
    Remove duplicates from a sorted array.

    :param arr: List of sorted integers
    :return: List with no duplicate elements
    """
    return list(set(arr))

# def remove_duplicates(my_list):
#     new_list = []
#     for item in my_list:
#         if item not in new_list:
#             new_list.append(item)
#     return new_list

#diger cevaplar için aynı sonucu verdi










