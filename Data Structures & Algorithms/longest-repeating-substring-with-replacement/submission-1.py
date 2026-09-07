class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        count = defaultdict(int)
        count[s[0]] += 1
        maxCount = 1
        maxFreq = 1
        l = r = 0
        while r < (len(s) - 1):
            r += 1
            count[s[r]] += 1
            maxFreq = max(maxFreq, count[s[r]])
            while (r - l + 1 - maxFreq) > k:
                count[s[l]] -= 1
                l += 1
            maxCount = max(maxCount, r - l + 1)
        
        return maxCount


            
        

        