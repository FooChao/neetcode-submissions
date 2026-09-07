class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set()
        def manhattan(point1, point2):
            return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
        
        cost = 0
        current = (0,points[0])
        currCost = [float('inf') for _ in points]
        while len(visited) < len(points):
            currentBest = float('inf')
            selectedPoint = None
            for i, point in enumerate(points):
                if i in visited:
                    continue
                currCost[i] = dst = min(manhattan(point, current[1]), currCost[i])
                if dst < currentBest:
                    currentBest = dst
                    selectedPoint = i
            cost += currentBest
            visited.add(selectedPoint)
            current = (selectedPoint, points[selectedPoint])
        return cost

                

