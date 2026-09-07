class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = [0] * (len(num1) + len(num2))
        for i in range(len(num1) -1, -1, -1):
            d1 = num1[i]
            for j in range(len(num2) -1, -1, -1):
                d2 = num2[j]
                offset = len(num1) -1 - i + len(num2) - 1 - j
                res[offset] += int(d1) * int(d2)
        
        print(res)
        carry = 0
        furthest = 0
        for i in range(0, len(num1) + len(num2)):
            res[i] += carry
            if res[i]:
                furthest = i
                carry = res[i] // 10
                res[i] %= 10
        
        res = res[0: furthest + 1]
        res.reverse()
        res = [str(i) for i in res]
        return "".join(res)


        
        