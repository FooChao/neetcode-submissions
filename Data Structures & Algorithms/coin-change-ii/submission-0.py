from functools import cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def dp(i ,remain):
            if remain == 0:
                return 1
            if i >= len(coins) or remain < 0:
                return 0
            coin = coins[i]
            count = 0
            while remain >= 0:
                count += dp(i + 1, remain)
                remain -= coin
            return count
        return dp(0, amount)


        