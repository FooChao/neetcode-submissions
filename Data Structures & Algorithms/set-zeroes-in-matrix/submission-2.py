class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        shouldTopBeZero = 0 in matrix[0]
        print(shouldTopBeZero)
        for i in range(1, len(matrix)):
            for j in range(0, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        print(matrix)
        
        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                for j in range(1, len(matrix[0])):
                    matrix[i][j] = 0
        
        for j in range(0, len(matrix[0])):
            if matrix[0][j] == 0:
                for i in range(1, len(matrix)):
                    matrix[i][j] = 0

        print(matrix)
        
        if shouldTopBeZero:
            for j in range(0, len(matrix[0])):
                matrix[0][j] = 0
        
        print(matrix)
        