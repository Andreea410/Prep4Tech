# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        setNodes = set()

        current = head
        while current:
            if current in setNodes:
                return True
            setNodes.add(current)
            current = current.next
        
        return False
