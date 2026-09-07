class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return max(nums[0], 0)
        bestRobPrev = 0
        bestNoRob = 0
        for i in range(0, len(nums) - 1):
            num = nums[i]
            temp = bestNoRob
            bestNoRob = max(bestNoRob, bestRobPrev)
            bestRobPrev = temp + num
        bestRobPrev2 = 0
        bestNoRob2 = 0
        for i in range(1, len(nums)):
            num = nums[i]
            temp = bestNoRob2
            bestNoRob2 = max(bestNoRob2, bestRobPrev2)
            bestRobPrev2 = temp + num
        return max(bestNoRob, bestRobPrev, bestNoRob2, bestRobPrev2)
        