class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        globalMax = nums[0]
        localPos = None
        localNeg = None

        for num in nums:
            print(num, localPos, localNeg, globalMax)
            if num > 0:
                localPos = localPos * num if localPos else num
                localNeg = localNeg * num if localNeg else None
            elif num == 0:
                localPos = None
                localNeg = None
                globalMax = 0 if globalMax < 0 else globalMax
            else:
                temp = localPos
                localPos = localNeg * num if localNeg else None
                localNeg = temp * num if temp else num
            
            if localPos:
                globalMax = max(localPos, globalMax)
            print(num, localPos, localNeg, globalMax, 'end')

        
        return globalMax
            


        