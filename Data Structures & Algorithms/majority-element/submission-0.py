class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        breakpoint = len(nums) // 2
        counts = Counter(nums)
        for k,v in counts.items():
            if v >= breakpoint:
                return k
        return None
        