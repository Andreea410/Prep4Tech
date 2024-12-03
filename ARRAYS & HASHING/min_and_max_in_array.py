# Given an array arr. Your task is to find the minimum and maximum elements in the array.

# Note: Return an array that contains two elements the first one will be a minimum element and the second will be a maximum of an array.

# Examples:

# Input: arr = [3, 2, 1, 56, 10000, 167]
# Output: 1 10000
# Explanation: minimum and maximum elements of array are 1 and 10000.
# Input: arr = [1, 345, 234, 21, 56789]
# Output: 1 56789
# Explanation: minimum and maximum element of array are 1 and 56789.
# Input: arr = [56789]
# Output: 56789 56789
# Explanation: Since the array contains only one element so both min & max are same.

class Solution:
    def get_min_max(self, arr):
        maximum = float('-inf')
        minimum = float('inf')
        
        for element in arr:
            if element > maximum:
                maximum = element
            if element < minimum:
                minimum =  element
        result = []
        result.append(minimum)
        result.append(maximum)
        return result

