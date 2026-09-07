class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        best = []
        position = 0
        while True:
            first = strs[0]
            if position >= len(first):
                return "".join(best)
            expected = first[position]
            for s in strs:
                if position >= len(s) or s[position] != expected:
                    return "".join(best)
                
            best.append(expected)
            position += 1
        
        return "".join(best)


                
                
            
        