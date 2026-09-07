class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        while low < high:
            time = 0
            m = (low + high) // 2
            for pile in piles:
                time += math.ceil(pile/m)
            print(low, high, m, time)
            if time > h:
                low = m + 1
            else:
                high = m
        
        return high


        