class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def helper(start, target):
            l, r = start, len(nums) - 1
            result = []
            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    result.append([nums[l], nums[r]])
                    l += 1
                    while l < len(nums) and nums[l] == nums[l - 1]:
                        l += 1
            return result
        
        nums.sort()
        curr = 0
        overall = []
        while curr < len(nums):
            if curr == 0 or nums[curr] != nums[curr - 1]:
                result = helper(curr + 1, 0 - nums[curr])
                for pair in result:
                    pair.append(nums[curr])
                    overall.append(pair)
            curr += 1
        return overall


                






        
        