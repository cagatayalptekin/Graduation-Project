#query="Write a program that takes two arrays and finds the elements present in the first array but not in the second array."
def find_missing_elements(arr1, arr2):
    return [element for element in arr1 if element not in arr2]