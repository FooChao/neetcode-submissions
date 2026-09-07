class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True
        nextTargetPos = 0
        visited = [
            [False for i in range(len(board[0]))] for j in range(len(board))
        ]
        def dfs(x, y):
            nonlocal nextTargetPos
            nonlocal visited
            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or visited[x][y]:
                return
            if not board[x][y] == word[nextTargetPos]:
                return
            if nextTargetPos == len(word) - 1:
                return True
            visited[x][y] = True
            nextTargetPos += 1
            result = dfs(x + 1, y) or dfs(x - 1, y) or dfs(x, y + 1) or dfs(x, y - 1)
            nextTargetPos -= 1
            visited[x][y] = False
            return result
        
        
        for x in range(len(board)):
            for y in range(len(board[0])):
                if (dfs(x,y)):
                    return True

        return False

            



        

