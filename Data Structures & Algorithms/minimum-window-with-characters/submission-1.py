class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countt = Counter(t)
        current = defaultdict(int)
        matched = 0
        neededMatch = len(t)
        globalMin = float('inf')
        minStringl = -1
        minStringr = -1
        l = 0
        for r, c in enumerate(s):
            # sliding right to find enough
            if c in countt and current[c] < countt[c]:
                matched += 1
            current[c] += 1

            # found a good substring
            if matched >= neededMatch:
                if r - l + 1 < globalMin:
                    globalMin = r - l + 1
                    minStringl = l
                    minStringr = r

                #slide left to invalidate it so we can find next best
                while matched >= neededMatch:
                    lc = s[l]
                    current[lc] -= 1
                    l += 1
                    if  lc in countt and current[lc] < countt[lc]:
                        matched -= 1
                    elif r - l + 1 < globalMin:
                        globalMin = r - l + 1
                        minStringl = l
                        minStringr = r
        
        return s[minStringl: minStringr + 1] if minStringl > -1 else ""
            