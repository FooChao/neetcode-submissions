class Solution:

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # helper function
        def daysNeeded(cap):
            # print(cap)
            current = 0
            days = 0

            for w in weights:
                # print('loop' ,w, current, days)
                if w > cap:
                    return float('inf')
                elif current + w > cap:
                    days += 1
                    current = w
                else:
                    current += w
                # print('loopend' ,w, current, days)
            # print(cap,days)
            return days + 1 if current > 0 else days
        
        # actual solution
        l, h = 1, sum(weights)

        while l < h:
            m = (l + h) // 2
            if daysNeeded(m) > days:
                l = m + 1
            else:
                h = m
        
        return h


        