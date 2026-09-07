class MedianFinder:

    def __init__(self):
        # filled first store key as positive (extra always come here)
        # filled with bigger numbers
        self.minHeap = []
        # filled next stored key as negative
        # filled with smaller numbers
        self.maxHeap = []
        self.count = 0    

    def addNum(self, num: int) -> None:
        # add to heap
        if self.count % 2 == 0:
            # fill to minHeap
            if (not self.maxHeap) or self.maxHeap[0][1] <= num:
                heapq.heappush(self.minHeap, (num, num))
            else:
                _, temp = heapq.heappop(self.maxHeap)
                heapq.heappush(self.minHeap, (temp, temp))
                heapq.heappush(self.maxHeap, (-num, num)) 
        else:
            # fill to maxHeap
            if self.minHeap[0][1] >= num:
                heapq.heappush(self.maxHeap, (-num, num))
            else:
                _, temp = heapq.heappop(self.minHeap)
                heapq.heappush(self.maxHeap, (-temp, temp))
                heapq.heappush(self.minHeap, (num, num)) 

        # increment count        
        self.count += 1

    def findMedian(self) -> float:
        print(self.minHeap, self.maxHeap)
        if self.count == 0:
            return None
        elif self.count % 2 == 0:
            return (self.minHeap[0][1] + self.maxHeap[0][1]) / 2
        else:
            return self.minHeap[0][1]

        
        
        