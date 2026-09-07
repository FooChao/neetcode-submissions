class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        visited = [False for _ in range(n)]

        def dfs(cur):
            nonlocal visited, adj
            if visited[cur]:
                return

            visited[cur] = True
            for i in adj[cur]:
                dfs(i)
        
        count = 0
        for i in range(n):
            if not visited[i]:
                count += 1
                dfs(i)
        return count


        