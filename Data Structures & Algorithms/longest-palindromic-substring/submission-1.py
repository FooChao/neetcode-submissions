class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        globalMax = 1
        globalMaxString = s[0]
        for i in range(1, len(s)):
            # odd size
            l, r = i - 1, i + 1
            print(l, r)
            while l >= 0 and r < len(s) and s[l] == s[r]:
                print("inner", l, r)
                if (r - l + 1) > globalMax:
                    print("bigger")
                    globalMax = r - l + 1
                    globalMaxString = s[l:r + 1]
                l -= 1
                r += 1
            
            # even size
            l, r = i - 1, i
            print(l, r)
            while l >= 0 and r < len(s) and s[l] == s[r]:
                print("inner", l, r)
                if (r - l + 1) > globalMax:
                    print("bigger")
                    globalMax = r - l + 1
                    globalMaxString = s[l:r + 1]
                l -= 1
                r += 1
            
        return globalMaxString






        