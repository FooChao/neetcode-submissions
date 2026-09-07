class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev = 0
        prevprev = 0
        cur = 0
        position = 2
        while position <= len(cost):
            cur = min(prev + cost[position - 1], prevprev + cost[position - 2])
            prev, prevprev = cur, prev
            position += 1
        return cur
        

        