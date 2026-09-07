class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        res = [0 for _ in temperatures]
        for i in range(len(temperatures) - 1, -1, -1):
            temperature = temperatures[i]
            while stk:
                if stk[-1][1] > temperature:
                    res[i] = stk[-1][0] - i
                    break
                else:
                    stk.pop()
            stk.append((i, temperature))
        return res
        