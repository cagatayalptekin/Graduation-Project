#Write a program that takes an array of numbers and finds the second largest (without sorting the entire array).
def second_largest(my_list):
    if len(my_list) < 2:
        return None
    second_largest = None
    for i in range(len(my_list)):
        if my_list[i] > my_list[0]:
            second_largest = my_list[i]
            break
    return second_largest