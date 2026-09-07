class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        mapLastToLength = defaultdict(int)
        for num in nums:
            bestLength = 1 # just itself
            for last, length in mapLastToLength.items():
                if last < num:
                    bestLength = max(bestLength, length + 1)
            mapLastToLength[num] = max(mapLastToLength[num], bestLength)
        return max(mapLastToLength.values())

        