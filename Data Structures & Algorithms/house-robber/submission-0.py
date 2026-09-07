class Solution:
    def rob(self, nums: List[int]) -> int:
        bestRobPrev = 0
        bestNoRob = 0
        for num in nums:
            print(num,bestNoRob, bestRobPrev)
            temp = bestNoRob
            bestNoRob = max(bestNoRob, bestRobPrev)
            bestRobPrev = temp + num
        return max(bestNoRob, bestRobPrev)
        