class Solution:
    def findCheapestPrice(
        self, 
        n: int, 
        flights: List[List[int]], 
        src: int, 
        dst: int, 
        k: int
    ) -> int:
        cost = [float('inf')] * n
        outFlights = [[] for _ in range(n)]
        for from_i, to_i, price_i in flights:
            outFlights[from_i].append((to_i, price_i))
        print(outFlights)
        
        # store as (cost, stop, location)
        pq = []

        pq.append((0, 0, src))
        while pq:
            print('start', pq)
            cost, stops, location = heapq.heappop(pq)
            print('start',cost,stops,location)
            if location == dst:
                print('reached',dst, cost)
                return cost
            if stops > k:
                print('too many stops')
                # if we take more than k stops to reach here and it is not dest, invalid
                continue

            outFlight = outFlights[location]
            print('outFlight', outFlight)
            for to, price in outFlight:
                print('outflight loop',to, price)
                heapq.heappush(pq, (price + cost, stops + 1, to))
            
        return -1
            

            
            

        