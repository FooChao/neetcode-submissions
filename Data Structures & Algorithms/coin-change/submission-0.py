from functools import cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def helper(i, remaining):
            print(i, remaining)
            if remaining == 0:
                return 0
            if remaining < 0 or i >= len(coins):
                return -1
            coin = coins[i]
            best = float('inf')
            count = 0
            while remaining >= 0:
                res = helper(i + 1, remaining)
                if res >= 0 and (res + count) < best:
                    best = res + count
                remaining -= coin
                count += 1
            
            return best if best != float('inf') else -1
        
        return helper(0, amount)
            
            
                
                
                
        