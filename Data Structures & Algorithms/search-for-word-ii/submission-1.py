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

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        tree = PrefixTree()
        res = set()
        for word in words:
            tree.insert(word)
        visited = set()
        currentVisited = []
        def dfs(x, y, prevNode):
            nonlocal currentVisited, visited, res

            if (
                x < 0 or 
                x >= len(board) or 
                y < 0 or 
                y >= len(board[0]) or 
                not board[x][y] in prevNode.children or
                (x,y) in visited
            ):
                return
            currentVisited.append(board[x][y])
            visited.add((x,y))
            node = prevNode.children[board[x][y]]
            if node.end:
                res.add("".join(currentVisited))
            dfs(x + 1, y, node)
            dfs(x - 1, y, node)
            dfs(x, y + 1, node)
            dfs(x, y - 1, node)
            visited.discard((x,y))
            currentVisited.pop()
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                print('--', i, j)
                dfs(i, j, tree.start)
        
        return [s for s in res]
        

            



        