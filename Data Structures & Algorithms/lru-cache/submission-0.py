class Node:
    def __init__(self, value, key, prev= None, nxt= None):
        self.value = value
        self.key = key
        self.nxt = nxt
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.firstNode = None
        self.lastNode = None
        self.remaining = capacity
        self.capacity = capacity
        self.hs = dict()

    def get(self, key: int) -> int:
        print('get', self.hs.keys())
        if key not in self.hs:
            print("not found")
            return -1
        node = self.hs[key]
        if not self.firstNode == node:
            if self.lastNode == node:
                self.lastNode = node.prev
            # move it to first
            prev = node.prev
            nxt = node.nxt
            if prev:
                prev.nxt = nxt
            if nxt:
                nxt.prev = prev
            node.nxt = self.firstNode
            self.firstNode = node
            node.prev = None
            if node.nxt:
                node.nxt.prev = node
        print(self.hs.keys())
        return node.value

    def put(self, key: int, value: int) -> None:
        print("put", self.hs.keys())
        if key in self.hs:
            self.hs[key].value = value
            self.get(key)
        else:
            # remove last node if needed
            if self.remaining == 0:
                ogLast = self.lastNode
                self.lastNode = self.lastNode.prev
                if ogLast:
                    self.hs.pop(ogLast.key)
                if self.firstNode == ogLast:
                    self.firstNode = None
            
            # add node to first
            prevFirst = self.firstNode
            self.firstNode = Node(value, key, None, prevFirst)
            if prevFirst:
                prevFirst.prev = self.firstNode
            self.hs[key] = self.firstNode

            if self.capacity == self.remaining:
                self.lastNode = self.firstNode
            if self.remaining:
                self.remaining -= 1
        print(self.hs.keys())
            
                


        
