class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if not total % 2 == 0:
            return False
        
        reachable = [True] + [False] * (total // 2)
        nextReachable = [r for r in reachable]
        for num in nums:
            nextReachable = [r for r in reachable]
            for i, r in enumerate(reachable):
                if r and (i + num) < len(reachable):
                    nextReachable[i + num] = True
            reachable = nextReachable
        return reachable[-1]


