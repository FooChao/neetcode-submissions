class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqTo = [[] for _ in range(numCourses)]
        for prereq in prerequisites:
            prereqTo[prereq[0]].append(prereq[1])
        
        def dfs(current, visited):
            print(current, visited, current in visited)
            if current in visited:
                print('gay')
                return False
            visited.add(current)
            for course in prereqTo[current]:
                if not dfs(course, visited):
                    return False
            visited.discard(current)
            return True
        
        for i in range(numCourses):
            print('start')
            if not dfs(i, set()):
                print('lesbian')
                return False
        
        return True

        
        
            
        