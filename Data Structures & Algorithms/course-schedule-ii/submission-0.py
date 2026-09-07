class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # set up
        prereqTo = [[] for i in range(0, numCourses)]
        indegs = [0 for i in range(0, numCourses)]
        for a, b in prerequisites:
            prereqTo[b].append(a)
            indegs[a] += 1
        currentLevel = [i for i, indeg in enumerate(indegs) if indeg == 0]
        
        # bfs
        nextLevel = []
        res = []
        while currentLevel:
            for i in currentLevel:
                res.append(i)
                postreq = prereqTo[i]
                for course in postreq:
                    indegs[course] -= 1
                    if indegs[course] == 0:
                        nextLevel.append(course)
            currentLevel, nextLevel = nextLevel, []
        print(res)
        return res if len(res) == numCourses else []