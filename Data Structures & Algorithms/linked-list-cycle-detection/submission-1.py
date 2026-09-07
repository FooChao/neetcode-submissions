# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        slow = head
        fast = head.next
        while slow != fast and fast != None:
            slow = slow.next
            fast = fast.next
            if fast != None:
                fast = fast.next
        
        return fast == slow
        