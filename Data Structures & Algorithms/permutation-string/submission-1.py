class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        s1Count = Counter(s1)
        s2Count = Counter(s2[0:len(s1)])
        l = 0
        r = len(s1)
        valid = True
        for k,v in s1Count.items():
            if k not in s2Count or s2Count[k] < v:
                valid  = False
                break
        if valid:
            return True

        while r < len(s2):
            if not s2Count[s2[r]]:
                s2Count[s2[r]] = 0
            s2Count[s2[r]] += 1
            s2Count[s2[l]] -= 1
            l += 1
            r += 1
            print(s1Count)
            print(s2Count)
            valid = True
            for k,v in s1Count.items():
                if k not in s2Count or s2Count[k] < v:
                    valid  = False
                    break
            if valid:
                return True
        return False


        
            