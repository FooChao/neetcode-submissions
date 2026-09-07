class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        reachable = [
            [[False, False] for _ in range(len(heights[0]))] for _ in range(len(heights))
        ]
        def dfs(x,y,z, previousHeight):
            if (x < 0 or 
                y < 0 or 
                x >= len(heights) or 
                y >= len(heights[0]) or 
                reachable[x][y][z] or
                heights[x][y] < previousHeight
            ):
                return
            reachable[x][y][z] = True
            h = heights[x][y]
            dfs(x + 1, y, z, h)
            dfs(x - 1, y, z, h)
            dfs(x ,y + 1, z, h)
            dfs(x ,y - 1, z, h)

        # mark pacific
        for i in range(len(heights[0])):
            dfs(0, i, 0, -float('inf'))

        for i in range(len(heights)):
            dfs(i, 0, 0, -float('inf'))

        # mark atlantic
        for i in range(len(heights[0])):
            dfs(len(heights) - 1, i, 1, -float('inf'))

        for i in range(len(heights)):
            dfs(i, len(heights[0]) - 1, 1, -float('inf'))

        res = []
        for i in range(len(reachable)):
            for j in range(len(reachable[0])):
                if reachable[i][j][0] and reachable[i][j][1]:
                    res.append([i,j])
        return res





        