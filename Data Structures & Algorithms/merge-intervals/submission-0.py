class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return intervals
        intervals.sort(key=lambda a: a[0])
        res = [intervals[0]]
        prev = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= prev[1]:
                prev[1] = max(prev[1], intervals[i][1])
            else:
                res.append(intervals[i])
                prev = intervals[i]
        return res
        
        
        