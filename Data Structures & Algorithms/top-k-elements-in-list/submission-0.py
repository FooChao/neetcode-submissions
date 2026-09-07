class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        bucket = [[] for _ in range(len(nums))]
        for key, value in count.items():
            bucket[value - 1].append(key)
        result = []
        for i in range(len(nums) - 1, -1, -1):
            lst = bucket[i]
            for ele in lst:
                result.append(ele)
            if len(result) >= k:
                return result
        return result

        
