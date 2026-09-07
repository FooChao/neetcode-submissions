class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        count = Counter(nums)
        nums.sort()
        current = []
        res = []
        print(nums, count)
        def helper(i, duplicateCount):
            print(i ,duplicateCount)
            if i >= len(nums):
                res.append(current.copy())
                return
            
            # we used it 
            num = nums[i]
            current.append(num)
            if i < len(nums) - 1 and nums[i + 1] == num:
                helper(i + 1, duplicateCount + 1)
            else:
                helper(i + 1, 0)
            current.pop()
            
            # we did not used it -> jump right to next unique count
            helper(i + count[num] - duplicateCount, 0)

        helper(0, 0)
        return res



        