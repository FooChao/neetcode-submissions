class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums[0:k])
        heap = [(-v, v) for v in count.keys()]
        heapq.heapify(heap)
        res = []
        for i in range(k , len(nums)):
            # add to res
            currentMax = heap[0][1]
            currentCount = count[currentMax]
            while currentCount <= 0:
                heapq.heappop(heap)
                currentMax = heap[0][1]
                currentCount = count[currentMax]
            res.append(currentMax)

            # shift window
            # add next
            n = nums[i]
            heapq.heappush(heap,(-n, n))
            if not n in count:
                count[n] = 0
            count[n] += 1

            # remove prev
            p = nums[i - k]
            count[p] -= 1
        
        # handle last one to add to res
        currentMax = heap[0][1]
        currentCount = count[currentMax]
        while currentCount <= 0:
            heapq.heappop(heap)
            currentMax = heap[0][1]
            currentCount = count[currentMax]
        res.append(currentMax)

        print(res)
        return res


            



                

        