class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[0: k]
        heapq.heapify(heap)
        for i in range (k, len(nums)):
            num = nums[i]
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)
        
        return heap[0]

        