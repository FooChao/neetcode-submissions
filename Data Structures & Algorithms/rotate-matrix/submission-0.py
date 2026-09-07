class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # reverse
        for i in range(0, len(matrix) // 2):
            for j in range(0, len(matrix[0])):
                top = matrix[i][j]
                matrix[i][j] = matrix[len(matrix) - 1 - i][j]
                matrix[len(matrix) - 1 - i][j] = top
        
        # transpose
        for i in range(0, len(matrix)):
            for j in range(i, len(matrix[0])):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        
        

