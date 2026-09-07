class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = dict()
        for i in range(0, len(nums)):
            num = nums[i]
            if (target - num) in visited:
                return [visited[target - num], i]
            else:
                visited[num] = i

