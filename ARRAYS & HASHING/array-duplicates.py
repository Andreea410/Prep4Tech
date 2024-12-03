# Given an array arr of integers, find all the elements that occur more than once in the array. Return the result in ascending order. If no element repeats, return an empty array.

# Examples:

# Input: arr[] = [2, 3, 1, 2, 3]
# Output: [2, 3] 
# Explanation: 2 and 3 occur more than once in the given array.
# Input: arr[] = [0, 3, 1, 2] 
# Output: [] 
# Explanation: There is no repeating element in the array, so the output is empty.
# Input: arr[] = [2]
# Output: [] 
# Explanation: There is single element in the array. Therefore output is empty.
# Constraints:
# 1 <= arr.size() <= 106
# 0 <= arr[i] <= 106

class Solution:
    def findDuplicates(self, arr):
        # code here
        count = {}
        result = []
        for element in arr:
            if element in count:
                result.append(element)
                count[element] += 1
            else:
                count[element] = 1
        
        
        result.sort()
        return result

