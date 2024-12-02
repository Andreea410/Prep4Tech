# Given an array of positive integers arr[] of size n,
# the task is to find second largest distinct element in the array.
# Note: If the second largest element does not exist, return -1.
# Examples:
#
# Input: arr[] = [12, 35, 1, 10, 34, 1]
# Output: 34
# Explanation: The largest element of the array is 35 and the second largest element is 34.
#
#
# Input: arr[] = [10, 5, 10]
# Output: 5
# Explanation: The largest element of the array is 10 and the second largest element is 5.
#
#
# Input: arr[] = [10, 10, 10]
# Output: -1
# Explanation: The largest element of the array is 10 there is no second largest element

def find_second_largest_element(arr):
    largest1 = -1
    largest2 = -1
    for element in arr:
        if element > largest1:
            largest2 = largest1
            largest1 = element
        elif element > largest2 and element!=largest1:
            largest2 = element
    if largest2 == largest1:
        return -1
    return largest2

if __name__ == '__main__':
    print(find_second_largest_element([12, 35, 1, 10, 34, 1]))


