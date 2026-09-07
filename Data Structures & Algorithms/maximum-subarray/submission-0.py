class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        globalMax = nums[0]
        localMax = 0
        for num in nums:
            localMax = max(localMax, 0) + num
            globalMax = max(localMax, globalMax)
        return globalMax
        