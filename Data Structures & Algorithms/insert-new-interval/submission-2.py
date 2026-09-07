class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        added = newInterval
        included = False
        res = []
        for interval in intervals:
            if added[0] < interval[0] and not included:
                res.append(added)
                included = True
            if interval[1] < added[0] or interval[0] > added[1]:
                # no overlap
                res.append(interval)
            else:
                # overlap 
                if not included:
                    res.append(added)
                    included = True
                added[0] = min(added[0], interval[0])
                added[1] = max(added[1], interval[1])
        if not included:
            res.append(added)
        return res
            

