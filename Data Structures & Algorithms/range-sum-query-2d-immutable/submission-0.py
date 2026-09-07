class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # sum from top left to spot
        self.sumAll = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
        self.matrix = matrix

        # calculate and update
        for i in range(0 , len(matrix)):
            for j in range(0 , len(matrix[0])):
                top = 0 if i == 0 else self.sumAll[i - 1][j]
                left = 0 if j == 0 else self.sumAll[i][j - 1]
                removed = 0 if i == 0 or j == 0 else self.sumAll[i-1][j-1]
                self.sumAll[i][j] = top + left + self.matrix[i][j] - removed

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # row is inner
        # col is outer
        whole = self.sumAll[row2][col2]
        topRemoved = 0 if col1 == 0 else self.sumAll[row2][col1 - 1]
        leftRemoved = 0 if row1 == 0 else self.sumAll[row1 - 1][col2]
        addBack = 0 if row1 == 0 or col1 == 0 else self.sumAll[row1 -1][col1 - 1]
        return whole - topRemoved - leftRemoved + addBack

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)