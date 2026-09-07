from functools import cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def dp(pos):
            if pos == len(s):
                return True
            if pos > len(s):
                return False
            
            remainingLen = len(s) - pos
            for w in wordDict:
                if len(w) <= remainingLen and w == s[pos: pos + len(w)] and dp(pos + len(w)):
                    return True
            
            return False
        
        return dp(0)



            
        