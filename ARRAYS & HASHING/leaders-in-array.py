# Given an array arr[] of size n, the task is to find all the Leaders in the array.
# An element is a Leader if it is greater than all the elements to its right side.
# Note: The rightmost element is always a leader.
#
# Examples:
#
# Input: arr[] = [16, 17, 4, 3, 5, 2]
# Output: [17 5 2]
# Explanation: 17 is greater than all the elements to its right i.e., [4, 3, 5, 2],
# therefore 17 is a leader. 5 is greater than all the elements to its right i.e., [2],
# therefore 5 is a leader. 2 has no element to its right, therefore 2 is a leader.
#
# Input: arr[] = [1, 2, 3, 4, 5, 2]
# Output: [5 2]
# Explanation: 5 is greater than all the elements to its right i.e., [2], therefore 5 is a leader. 2 has no element to its right, therefore 2 is a leader.
#

def find_leaders(arr):
    largest_from_right = arr[len(arr)-1]
    largest = [largest_from_right]
    for i in range(len(arr)-2,-1,-1):
        if arr[i] > largest_from_right:
            largest.append(arr[i])
            largest_from_right = arr[i]
    largest.reverse()
    return largest

if __name__ == '__main__':
    print(find_leaders([16,17,4,3,5,2]))
