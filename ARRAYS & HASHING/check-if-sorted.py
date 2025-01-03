# Given an array of size n, the task is to check if it is sorted in ascending order or not.
# Equal values are allowed in an array and two consecutive equal values are considered sorted.
#
# Examples:
#
# Input: arr[] = [20, 21, 45, 89, 89, 90]
# Output: Yes
#
# Input: arr[] = [20, 20, 45, 89, 89, 90]
# Output: Yes
#
# Input: arr[] = [20, 20, 78, 98, 99, 97]
# Output: No


def check_if_sorted(arr):
    last_element = -1
    for element in arr:
        if element < last_element:
            return False
        last_element = element
    return True

if __name__ == '__main__':
    print(check_if_sorted([20, 20, 45, 89, 89, 90]))