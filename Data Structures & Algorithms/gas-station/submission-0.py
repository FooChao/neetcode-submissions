class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        rem = 0
        res = 0
        for i in range(len(gas)):
            if rem < 0:
                res = i
                rem = 0
            rem += gas[i]
            rem -= cost[i]
        return res
        