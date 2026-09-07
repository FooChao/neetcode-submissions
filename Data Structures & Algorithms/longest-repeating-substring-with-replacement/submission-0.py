class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        count = defaultdict(int)
        count[s[0]] += 1
        maxCount = 1
        l = r = 0
        while r < (len(s) - 1):
            r += 1
            count[s[r]] += 1
            while (r - l + 1 - max(count.values())) > k:
                count[s[l]] -= 1
                l += 1
            maxCount = max(maxCount, r - l + 1)
        
        return maxCount


            
        

        