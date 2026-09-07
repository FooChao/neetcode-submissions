class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        print(nums)
        res = []
        current = []
        def helper(l,remaining):
            nonlocal nums, current, res
            if l >= len(nums):
                return
            if remaining == 0:
                added = [i for i in current]
                res.append(added)
                return
            if remaining < 0:
                return

            num = nums[l]
            
            # case 1 not used
            helper(l + 1, remaining)

            # case 2 used
            current.append(num)
            helper(l, remaining - num)
            current.pop()

        helper(0, target)
        return res

            
        