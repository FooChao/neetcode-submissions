class Solution:
    def findMinIndex(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        return l
    
    def search(self, nums: List[int], target: int) -> int:
        pivot = self.findMinIndex(nums)
        if nums[pivot] > target:
            return -1
        if nums[pivot] == target:
            return pivot
        
        # so pivot less than target
        if nums[-1] < target:
            l,r = 0, max(pivot - 1, 0)
        else:
            l,r = min(pivot + 1, len(nums) - 1), len(nums) - 1
        
        # now both case is strictly increasing so can do normal binary search
        while l < r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        
        return l if nums[l] == target else -1



        
        
        