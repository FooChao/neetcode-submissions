class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        chosen = [False for _ in nums]
        res = []

        def dfs(cur):
            if len(cur) == len(nums):
                res.append(cur.copy())
            
            for i, num in enumerate(nums):
                isItChosen = chosen[i]
                if not isItChosen:
                    cur.append(num)
                    chosen[i] = True
                    dfs(cur)
                    cur.pop()
                    chosen[i] = False
        
        dfs([])
        return res

        