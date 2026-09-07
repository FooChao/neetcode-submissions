class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        currentMaxLength = 0
        visited = set()
        left = 0
        for i, c in enumerate(s):
            if c in visited:
                while s[left] != c:
                    visited.discard(s[left])
                    left += 1
                left += 1
            visited.add(c)
            currentMaxLength = max(i - left + 1, currentMaxLength)
        return currentMaxLength






        