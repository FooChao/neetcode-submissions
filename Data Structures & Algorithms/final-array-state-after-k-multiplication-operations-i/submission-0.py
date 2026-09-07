class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [(num, i) for (i,num) in enumerate(nums)]
        heapq.heapify(heap)
        for _ in range(k):
            print(heap, nums)
            num, i = heapq.heappop(heap)
            nums[i] = nums[i] * multiplier
            heapq.heappush(heap, (nums[i], i))
        return nums

        