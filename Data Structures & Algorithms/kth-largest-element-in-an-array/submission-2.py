class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heap = nums[0: k]
        # heapq.heapify(heap)
        # for i in range (k, len(nums)):
        #     num = nums[i]
        #     if num > heap[0]:
        #         heapq.heappop(heap)
        #         heapq.heappush(heap, num)
        
        # return heap[0]

        l ,r = 0, len(nums) - 1
        k = len(nums) - k
        print(k)

        while l < r:
            pivot = nums[l]
            print(l, r, nums, nums[l])
            l1 = l + 1
            r1 = r
            while l1 < r1:
                print(l1, r1, nums[l1], pivot)
                # left < pivot
                if nums[l1] < pivot:
                    print('left < pivot')
                    l1 += 1
                    continue
                
                # left > pivot
                # find a right < pivot
                if nums[r1] < pivot:
                    print('swapping')
                    # swap left and right
                    nums[r1], nums[l1] = nums[l1], nums[r1]
                    l1 += 1
                else:
                    print('r1 > pivot')
                    r1 -= 1
            
            # swap pivot with the one in front of l1 since l1 > pivot
            if nums[r1] < nums[l]: # edge case all smaller
                nums[l], nums[r] = nums[r], nums[l]
                pivotPosition = r
            else:
                nums[r1 - 1], nums[l] = nums[l], nums[r1 - 1]
                pivotPosition = r1 - 1
            if pivotPosition == k:
                print('pivotPos', pivotPosition, nums)
                return nums[pivotPosition]
            elif pivotPosition > k:
                r = pivotPosition - 1
            else: 
                l = pivotPosition + 1

        if l == k:
            return nums[l]
        return nums[r]
        

                



        