class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        hsh = {
            '2': [chr(ord('a') + i) for i in range(0,3)],
            '3': [chr(ord('d') + i) for i in range(0,3)],
            '4': [chr(ord('g') + i) for i in range(0,3)],
            '5': [chr(ord('j') + i)for i in range(0,3)],
            '6': [chr(ord('m') + i)for i in range(0,3)],
            '7': [chr(ord('p') + i)for i in range(0,4)],
            '8': [chr(ord('t') + i)for i in range(0,3)],
            '9': [chr(ord('w') + i)for i in range(0,4)],
        }

        def combi(current):
            if current >= len(digits):
                return ['']
            validCurrentChar = hsh[digits[current]]
            behindCombi = combi(current + 1)
            res = []
            for c in validCurrentChar:
                for b in behindCombi:
                    added = c + b
                    res.append(added)

            return res
        
        return combi(0)


        