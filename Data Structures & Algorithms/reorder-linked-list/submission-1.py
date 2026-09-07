# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head == None or head.next == None:
            return

        # count length
        count = 0
        current = head
        while current != None:
            count += 1
            current = current.next

        print(count)
        
        # split to 2 groups
        size1 = count // 2 + count % 2
        print(size1)

        list1 = head
        list2 = head

        while size1 > 1:
            list2 = list2.next
            size1 -= 1

        temp = list2
        list2 = list2.next
        temp.next = None

        # flip list 2
        current = list2
        prev = None
        while current != None:
            temp = current
            current = current.next
            temp.next = prev
            prev = temp
        
        list2 = prev

        combined = ListNode()
        current = combined
        while list1:
            current.next = list1
            list1 = list1.next
            current = current.next
            if list2:
                current.next = list2
                list2 = list2.next
                current = current.next
        
        return
            