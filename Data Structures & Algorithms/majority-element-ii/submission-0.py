class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        breakpoint = len(nums) // 3
        counts = Counter(nums)
        res = []
        for k,v in counts.items():
            if v > breakpoint:
                res.append(k)
        return res


        
        