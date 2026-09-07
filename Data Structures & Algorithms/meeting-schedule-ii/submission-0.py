"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # end -> 0
        # start -> 1
        event = []
        for i in intervals:
            event.append((i.start, 1))
            event.append((i.end, 0))
        
        event.sort()
        count = 0
        globalMax = 0
        for e in event:
            if e[1] == 1:
                count += 1
                globalMax = max(globalMax, count)
            else:
                count -= 1
        return globalMax



        