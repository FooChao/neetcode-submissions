"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        mapOldToNew = dict()
        oldCur = head
        newCur = Node(head.val, None, None)
        newHead = newCur
        mapOldToNew[oldCur] = newCur
        # iter 1 normal pointer
        while oldCur:
            oldNext = oldCur.next
            newNext = None
            if oldNext:
                newNext = Node(oldNext.val, None, None)
                mapOldToNew[oldNext] = newNext
                newCur.next = newNext
            oldCur = oldNext
            newCur = newNext
        
        
        # iter 2 random pointer
        oldCur = head
        newCur = newHead
        while oldCur:
            if oldCur.random:
                newCur.random = mapOldToNew[oldCur.random]
            oldCur = oldCur.next
            newCur = newCur.next
        
        return newHead

            
        