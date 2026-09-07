class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [-float('inf') for _ in range(len(height))]
        maxRight = [-float('inf') for _ in range(len(height))]
        currentL = -float('inf')
        currentR = -float('inf')
        for i in range(0, len(height)):
            maxLeft[i] = currentL
            maxRight[len(height) - i - 1] = currentR
            currentL = max(height[i], currentL)
            currentR = max(height[len(height) - i - 1], currentR)

        area = 0
        for i in range(0, len(height)):
            h = height[i]
            if h < maxLeft[i] and h < maxRight[i]:
                area += min(maxLeft[i], maxRight[i]) - h
        
        return area


