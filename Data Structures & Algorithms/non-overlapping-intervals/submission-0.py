class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda a: -a[0])
        endBefore = float('inf')
        count = 0
        for interval in intervals:
            print(interval, endBefore)
            if interval[1] <= endBefore:
                endBefore = interval[0]
            else:
                count += 1
        return count

        