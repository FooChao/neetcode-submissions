from functools import cache
class Solution:

    def numDecodings(self, s: str) -> int:
        @cache
        def helper(index):
            if index >= len(s):
                # reached end
                return 1
            if s[index] == "0":
                return 0
            count = helper(index + 1)
            if index < (len(s) - 1):
                substring = s[index:index + 2]
                if int(substring) <= 26:
                    count += helper(index + 2)
            return count
        return helper(0)
        