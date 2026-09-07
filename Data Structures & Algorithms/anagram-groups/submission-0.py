class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = dict()
        for str in strs:
            freqArray = [0 for _ in range(26)]
            for char in str:
                freqArray[ord(char) - ord('a')] += 1
            if tuple(freqArray) in hash:
                hash[tuple(freqArray)].append(str)
            else:
                hash[tuple(freqArray)] = [str]
        return list(hash.values())

            
