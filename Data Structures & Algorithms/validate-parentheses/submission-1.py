class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            elif c == ")":
                if len(stack) == 0:
                    return False
                out = stack.pop()
                if out != "(":
                    return False
            elif c == "]":
                if len(stack) == 0:
                    return False
                out = stack.pop()
                if out != "[":
                    return False
            elif c == "}":
                if len(stack) == 0:
                    return False
                out = stack.pop()
                if out != "{":
                    return False
            else:
                return False
        
        return True if len(stack) == 0 else False
            

        