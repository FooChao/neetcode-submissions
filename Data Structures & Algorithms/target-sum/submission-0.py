from functools import cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def dp(i ,cur):
            if i == len(nums):
                return 1 if target == cur else 0
            num = nums[i]
            return dp(i + 1, cur + num) + dp(i + 1, cur - num)
        return dp(0, 0)

        
        