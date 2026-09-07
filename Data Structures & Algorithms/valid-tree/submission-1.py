class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        mapper = [set() for _ in range(n)]
        
        for e in edges:
            mapper[e[0]].add(e[1])
            mapper[e[1]].add(e[0])

        count = 0
        visited = set()
        
        def dfs(current):
            nonlocal count, visited, mapper
            print(count, visited, mapper)
            if current in visited or count >= n:
                print(current, visited, mapper)
                return False
            visited.add(current)
            count += 1
            
            for v in mapper[current]:
                mapper[v].discard(current)
                if not dfs(v):
                    return False
            
            return True

        return dfs(0) and count == (n)
        

            
        