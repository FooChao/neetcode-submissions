class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        turn = 0
        turnMax = 0
        nextMax = 0
        current = 0
        while nextMax < len(nums) - 1:
            if current > turnMax:
                turn += 1
                turnMax = nextMax
            else:
                jump = nums[current]
                nextMax = max(nextMax, current + jump)
                current += 1
        return turn + 1

        