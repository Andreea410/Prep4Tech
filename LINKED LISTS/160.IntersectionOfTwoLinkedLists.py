# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        current1 = headA
        setValues = set()
        while current1:
            setValues.add(current1)
            current1 = current1.next
        
        current2 = headB

        while current2:
            if current2 in setValues:
                return current2
            current2 = current2.next
        
        return None
