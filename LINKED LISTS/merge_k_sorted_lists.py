# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

 

# Example 1:

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
# Example 2:

# Input: lists = []
# Output: []
# Example 3:

# Input: lists = [[]]
# Output: []
 

# Constraints:

# k == lists.length
# 0 <= k <= 104
# 0 <= lists[i].length <= 500
# -104 <= lists[i][j] <= 104
# lists[i] is sorted in ascending order.
# The sum of lists[i].length will not exceed 104.

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if len(lists) < 1:
            return None
        if len(lists) == 1:
            return lists[0]
        pointer_list = len(lists) -1

        def merge_lists(l1,l2):
            dummy = ListNode()
            tail = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next
            
            while l1:
                tail.next = l1
                l1 = l1.next 
                tail = tail.next
            while l2:
                tail.next = l2
                l2 = l2.next
                tail = tail.next
            return dummy.next
        
        while pointer_list > 0:
            first_list = lists.pop()
            second_list = lists.pop()
            merged_list = merge_lists(first_list,second_list)
            lists.append(merged_list)
            pointer_list -= 1
        
        return lists[0]
        
        



        
