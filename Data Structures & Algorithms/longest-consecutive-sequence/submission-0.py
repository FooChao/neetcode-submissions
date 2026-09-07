class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash = set(nums)
        globalMax = 0
        for num in hash:
            if not num - 1 in hash:
                count = 1
                while num + count in hash:
                    count += 1
                globalMax = max(globalMax, count)
        return globalMax
             
        