class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) * len(matrix[0]) - 1
        while l < r:
            m = (l + r) // 2
            row, col = m // len(matrix[0]), m % len(matrix[0])
            print(m, row, col)
            num = matrix[row][col]
            if num == target:
                return True
            elif num < target:
                l = m + 1
            else:
                r = m
        
        row, col = r // len(matrix[0]), r % len(matrix[0])
        return matrix[row][col] == target
        


        