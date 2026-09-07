class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        if len(words) == 0:
            return ""
        if len(words) == 1:
            return words[0]
        isAfterCount = defaultdict(int)
        isBeforeMap = defaultdict(set)
        for j in range(1, len(words)):
            prev = words[j - 1]
            curr = words[j]
            print(j, prev, curr)


            hasFoundDiff = False
            for i in range(0, max(len(prev), len(curr))):
                print(hasFoundDiff, i, prev, curr)
                if (not hasFoundDiff and 
                    i < len(prev) and 
                    i < len(curr) and
                    prev[i] != curr[i]
                ):
                    hasFoundDiff = True
                    if not curr[i] in isBeforeMap[prev[i]]:
                        isAfterCount[curr[i]] += 1
                        isBeforeMap[prev[i]].add(curr[i])
                
                if not hasFoundDiff and i < len(prev) and i >= len(curr):
                    return ""

                
                if i < len(prev):
                    isAfterCount[prev[i]] = isAfterCount[prev[i]] if prev[i] in isAfterCount else 0
                    isBeforeMap[prev[i]] = isBeforeMap[prev[i]] if prev[i] in isBeforeMap else set()

                
                if i < len(curr):
                    isAfterCount[curr[i]] = isAfterCount[curr[i]] if curr[i] in isAfterCount else 0
                    isBeforeMap[curr[i]] = isBeforeMap[curr[i]] if curr[i] in isBeforeMap else set()
            
        remainingLetter = len(isAfterCount.values())
        potentialNextLetter = []

        for k,v in isAfterCount.items():
            if v == 0:
                potentialNextLetter.append(k)
        
        resList = []
        while len(potentialNextLetter):
            l = potentialNextLetter.pop()
            resList.append(l)
            remainingLetter -= 1
            for m in isBeforeMap[l]:
                isAfterCount[m] -= 1
                if isAfterCount[m] == 0:
                    potentialNextLetter.append(m)
        return "" if remainingLetter > 0 else "".join(resList)
                    




                    

                    

        