# Given an array arr[], the task is to find the top three largest distinct integers present in the array.
#
# Note: If there are less than three distinct elements in the array, then return the available distinct numbers in descending order.
#
# Examples :
#
# Input: arr[] = [10, 4, 3, 50, 23, 90]
# Output: [90, 50, 23]
#
#
# Input: arr[] = [10, 9, 9]
# Output: [10, 9]
# There are only two distinct elements
#
#
# Input: arr[] = [10, 10, 10]
# Output: [10]
# There is only one distinct element
#
#
# Input: arr[] = []
# Output: []

def top_three_largest(arr):
    result = []
    first =-1
    second = -1
    third = -1

    for element in arr:
        if element > first:
            third = second
            second = first
            first = element
        elif element > second and element!= first:
            third = second
            second = element
        elif element > third and element != second and element != first:
            third = element

    if first!=-1:
        result.append(first)
    if second != -1:
        result.append(second)
    if third != -1:
        result.append(third)
    return result

if __name__ == '__main__':
    print(top_three_largest([10,4,3,50,23,90]))
