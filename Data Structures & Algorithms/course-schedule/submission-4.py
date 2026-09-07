class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqTo = [[] for _ in range(numCourses)]
        for prereq in prerequisites:
            prereqTo[prereq[0]].append(prereq[1])
        
        def dfs(current, visited):
            if current in visited:
                return False
            visited.add(current)
            for course in prereqTo[current]:
                if not dfs(course, visited):
                    return False
            visited.discard(current)
            prereqTo[current] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i, set()):
                return False
        
        return True

        
        
            
        