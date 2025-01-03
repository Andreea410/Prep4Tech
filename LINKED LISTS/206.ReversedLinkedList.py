# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        current = head
        last_element = ListNode(current.val)
        current = current.next
        while current:
            new_current = ListNode(current.val)
            new_current.next = last_element
            last_element = new_current
            current = current.next
        
        return last_element
