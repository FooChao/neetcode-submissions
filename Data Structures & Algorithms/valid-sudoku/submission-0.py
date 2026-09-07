class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check row
        for i in range(0,9):
            visited = set()
            for j in range(0,9):
                if not board[i][j] == "." and board[i][j] in visited:
                    return False
                visited.add(board[i][j])
        
        # check col
        for j in range(0,9):
            visited = set()
            for i in range(0,9):
                if not board[i][j] == "." and board[i][j] in visited:
                    return False
                visited.add(board[i][j])
        
        # check box
        for i in range(0,9,3):
            for j in range(0,9,3):
                visited = set()
                for k in range(0,3):
                    for l in range(0,3):
                        if not board[i + k][j + l] == "." and board[i + k][j + l] in visited:
                            return False
                        visited.add(board[i + k][j + l])
        
        return True
