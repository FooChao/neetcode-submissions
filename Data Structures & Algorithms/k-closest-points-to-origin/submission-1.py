class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(point: List[int]) -> int:
            return (point[0] ** 2 + point[1] ** 2) ** 0.5
        
        # max heap (-dist, index, point)
        hp = [ (- dist(point), i, point)for i, point in enumerate(points[0: k])]
        heapq.heapify(hp)

        for i in range(k, len(points)):
            point = points[i]
            d = dist(point)
            hpMax = -hp[0][0]
            print(d, hpMax)
            if d < hpMax:
                heapq.heappop(hp)
                heapq.heappush(hp, (-d, i, point))
        
        return [x[2] for x in hp]




         