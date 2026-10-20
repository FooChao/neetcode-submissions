# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        
        temp = ListNode(0, head)
        current = temp
        following = head
        beforeLeftMost = None
        leftMost = None
        # print('hi')
        for i in range(1, right + 1):
            # print("current", current.val, i , left)
            # check if need to set left most
            if i == left:
                beforeLeftMost = current
                # print(beforeLeftMost.val)
                leftMost = following
                # print(leftMost.val)
            
            # shift forward
            previous = current
            current = following
            following = following.next

            #swap arrow side
            if i >= left:
                current.next = previous
        
        # print(beforeLeftMost.val, current.val, leftMost.val, following)
        beforeLeftMost.next = current
        leftMost.next = following
        return temp.next


            

                



