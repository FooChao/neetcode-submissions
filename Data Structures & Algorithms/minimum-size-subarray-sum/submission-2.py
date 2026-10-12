class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        found = False
        best = 0
        l = r = 0
        current = nums[0]
        if current >= target:
            return 1
        while r < len(nums):
            # print (l,r,current)
            if current >= target:
                # print('found')
                best = min(r - l + 1, best) if found else r - l + 1
                found = True
                # print('best', best)
                current -= nums[l]
                l += 1
            else:
                r += 1
                current = current if r == len(nums) else current + nums[r]
        return best

            

        
        