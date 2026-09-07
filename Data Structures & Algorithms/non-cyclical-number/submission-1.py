class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        def helper(n):
            print(n, visited)
            if n in visited:
                return False
            
            string = str(n)
            j = 0
            for c in string:
                j += int(c) ** 2
            
            if j == 1:
                return True
            
            visited.add(n)
            return helper(j)
        
        return helper(n)

        