class Solution:
    def countBits(self, n: int) -> List[int]:
        prevFullFlip = 0
        nextFullFlip = 1
        res = [0]
        for i in range(1, n + 1):
            if i == nextFullFlip:
                res.append(1)
                prevFullFlip = nextFullFlip
                nextFullFlip = prevFullFlip * 2
            else:
                res.append(res[prevFullFlip] + res[i - prevFullFlip])
        return res


        