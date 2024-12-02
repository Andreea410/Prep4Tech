# Given an array arr[] of size n, the task is to find the largest element in the given array.
#
# Examples:
#
# Input: arr[] = {10, 20, 4}
# Output: 20
# Explanation: Among 10, 20 and 4, 20 is the largest.
#
#
# Input : arr[] = {20, 10, 20, 4, 100}
# Output : 100
#

def find_largest_element(arr):
    maximum = float('-inf')
    for element in arr:
        maximum = max(element,maximum)
    return maximum

if __name__ == '__main__':
    print(find_largest_element([20,10,4,20,100]))
