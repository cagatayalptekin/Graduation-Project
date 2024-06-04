#Write a program that rotates an array by a specified number of positions (to the left or right).
def rotate_array(arr, n):
    if n < 0:
        arr = arr[-n:] + arr[:-n]
    else:
        arr = arr[n:] + arr[:n]
    return arr

