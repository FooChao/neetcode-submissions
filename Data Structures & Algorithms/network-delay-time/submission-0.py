class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # set up adjacency list
        adj = {i : [] for i in range(1,n + 1)}
        for time in times:
            # store as a tuple (target, time)
            adj[time[0]].append((time[1], time[2]))
        
        # djikstra
        visited = set()
        pq = []
        timeFromSource = [float('inf')] * n
        timeFromSource[k - 1] = 0
        # (time from source, node)
        pq.append((0, k))
        while pq:
            cur = heapq.heappop(pq)
            if cur in visited:
                continue
            dst = cur[0]
            lst = adj[cur[1]]
            for target, time in lst:
                if timeFromSource[target - 1] > (time + dst):
                    timeFromSource[target - 1] = time + dst
                    heapq.heappush(pq, (timeFromSource[target - 1], target))
        
        print(timeFromSource)
        return -1 if max(timeFromSource) == float('inf') else max(timeFromSource)


