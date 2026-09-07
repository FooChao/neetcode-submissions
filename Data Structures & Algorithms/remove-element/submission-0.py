class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums)
        start, end = 0, len(nums) - 1
        while start <= end:
            if nums[start] == val:
                if nums[end] != val:
                    nums[start] = nums[end]
                    end = end - 1
                    start = start + 1
                    k -= 1
                else:
                    end = end - 1
                    k -= 1
            else:
                start = start + 1
        
        return k

        