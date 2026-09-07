class Node:
    def __init__(self, val, prev= None, next = None):
        self.val = val
        self.prev = prev
        self.next = next

class MinStack:

    def __init__(self):
        self.minstk = []
        self.stk = []

    def push(self, val: int) -> None:
        if len(self.minstk) == 0:
            self.minstk.append(val)
        else:
            self.minstk.append(min(val, self.minstk[-1]))
        self.stk.append(val)
        
    def pop(self) -> None:
        self.minstk.pop()
        self.stk.pop()

    def top(self) -> int:
        return self.stk[-1]
        
    def getMin(self) -> int:
        return self.minstk[-1]
        
