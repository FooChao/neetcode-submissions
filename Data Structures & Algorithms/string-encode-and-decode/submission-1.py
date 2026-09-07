class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ''
        for string in strs:
            result += (str(len(string)) + "#") + string
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        current = 0
        currentNumberRepresentation = ''
        while current < len(s):
            if s[current] != '#':
                currentNumberRepresentation += s[current]
                current += 1
            else:
                length = int(currentNumberRepresentation)
                result.append(s[current + 1: current + length + 1])
                current = current + length + 1
                currentNumberRepresentation = ''
        return result




