class Node:
    def __init__(
        self, 
        value: Optional[str] | None = None, 
        children: dict[str, "Node"] | None = None, 
        end : bool = False
    ):
        self.value = value
        self.children = children if children != None else {}
        self.end = end

class PrefixTree:

    def __init__(self):
        self.start = Node()

    def insert(self, word: str) -> None:
        curr = self.start
        for c in word:
            if not c in curr.children:
                curr.children[c] = Node(c)
            curr = curr.children[c]
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.start
        for c in word:
            if not c in curr.children:
                return False
            curr = curr.children[c]
        return curr.end
        
    def startsWith(self, prefix: str) -> bool:
        curr = self.start
        for c in prefix:
            if not c in curr.children:
                return False
            curr = curr.children[c]
        return True
        
        