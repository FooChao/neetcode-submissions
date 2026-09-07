class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # l -> first one that is potentially not 0
        # p -> iter pointer
        # r -> last one everything behind it is 2
        l, p, r = 0, 0, len(nums) - 1
        while p <= r:
            # print(nums)
            if nums[p] == 0:
                #swap it with l
                nums[p] = nums[l]
                nums[l] = 0
                p += 1
                l += 1
            elif nums[p] == 1:
                p += 1
            else:
                nums[p] = nums[r]
                nums[r] = 2
                r -= 1





        