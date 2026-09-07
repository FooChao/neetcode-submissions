class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0
        count = 1
        for i in range(1, len(s)):
            # odd size
            l, r = i, i
            print(l, r)
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            
            # even size
            l, r = i - 1, i
            print(l, r)
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            
        return count
        