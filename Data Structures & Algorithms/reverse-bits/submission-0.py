class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        mask = 1
        for i in range(0, 32):
            if n & (mask << i):
                res += mask << 31 - i
        return res
        