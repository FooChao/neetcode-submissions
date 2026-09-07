from functools import cache
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def reach(i , j):
            if i < 0 or j < 0 or i >= m or j >= n:
                return 0
            if i == 0 and j == 0:
                return 1
            return reach(i - 1, j) + reach(i, j - 1)
        
        return reach(m - 1, n - 1)

        