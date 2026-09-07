class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        print(candidates)
        res = []
        def dfs(pos, cur, rem):
            if rem == 0:
                res.append([i for i in cur])
                return
            if pos >= len(candidates) or rem < 0:
                return
            
            duplicateCount = 1
            while (
                (pos + duplicateCount) < len(candidates)and 
                candidates[pos] == candidates[pos + duplicateCount]
            ):
                duplicateCount += 1

            for i in range(0, duplicateCount):
                dfs(pos + duplicateCount, cur, rem)
                cur.append(candidates[pos])
                rem -= candidates[pos]
            dfs(pos + duplicateCount, cur, rem)

            for i in range(0, duplicateCount):
                print('pop')
                cur.pop()
        
        dfs(0, [], target)
        return res

            


