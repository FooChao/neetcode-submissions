class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1 for i in range(0, len(nums))]
        front = 1
        back = 1

        for i in range(0, len(nums)):
            num = nums[i]
            result[i] *= front
            front *= num
        
        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            result[i] *= back
            back *= num

        return result
        