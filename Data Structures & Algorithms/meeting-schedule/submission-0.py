"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda a: a.start)
        startAfter = -float('inf')
        for interval in intervals:
            if interval.start < startAfter:
                return False
            else:
                startAfter = max(startAfter, interval.end)
        return True
