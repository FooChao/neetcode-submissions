class Solution:
    def maxArea(self, heights: List[int]) -> int:
        globalMax = 0
        l, r = 0 , len(heights) - 1
        while l < r:
            if heights[l] > heights[r]:
                globalMax = max(globalMax, heights[r] * (r - l))
                r -= 1
            else:
                globalMax = max(globalMax, heights[l] * (r - l))
                l += 1

        return globalMax
        