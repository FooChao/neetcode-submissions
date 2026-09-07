# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        front = head
        back = head

        remain = n
        while remain > 0:
            back = back.next
            remain -= 1
        
        while back and back.next:
            back = back.next
            front = front.next


        if back == None:
            return head.next

        front.next = front.next.next
        return head
        