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

class WordDictionary:

    def __init__(self):
        self.start = Node()
        
    def addWord(self, word: str) -> None:
        curr = self.start
        for c in word:
            if not c in curr.children:
                curr.children[c] = Node(c)
            curr = curr.children[c]
        curr.end = True
        

    def search(self, word: str) -> bool:
        print(word, '----------------------------------')
        def helper(location: int, node: "Node") -> bool:
            nonlocal word
            if location == (len(word)):
                print('A')
                return node.end
            c = word[location]
            print(c, node.value)
            if c == '.':
                print('B')
                for child in node.children.values():
                    if helper(location + 1, child):
                        return True
                return False
            else:
                if not c in node.children:
                    print('c')
                    return False
                else:
                    print('d')
                    return helper(location + 1, node.children[c])
        return helper(0, self.start)

                    



        
