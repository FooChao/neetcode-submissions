class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        localCount = 0
        maxCount = 0

        def dfs(i, j):
            if i< 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or not grid[i][j]:
                return
            
            nonlocal localCount
            localCount += 1
            grid[i][j] = 0
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                localCount = 0
                dfs(i, j)
                maxCount = max(maxCount, localCount)
        
        return maxCount


        