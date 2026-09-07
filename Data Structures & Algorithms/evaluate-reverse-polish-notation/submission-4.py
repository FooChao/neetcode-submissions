class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        stack = [[tokens.pop()]]

        # approach 
        # push all ops (in an array) into stack in form ["*"]
        # if number push onto last array in stack
        # if last array size == 3 -> compute
        temp = 0
        while len(stack) > 0:
            #  step 1: extract the next value
            if len(stack[-1]) == 3: # can compute
                last = stack.pop()
                if last[0] == "+":
                    temp = int(last[1]) + int(last[2])
                elif last[0] == "-":
                    temp = int(last[2]) - int(last[1])
                elif last[0] == "*":
                    temp = int(last[1]) * int(last[2])
                else:
                    temp = int(last[2]) / int(last[1]) # because we start from back
                    if temp > 0:
                        temp = math.floor(temp)
                    else:
                        temp = math.ceil(temp)
                # standardise format
                temp = str(temp)
            elif len(tokens) > 0: # need get another one from tokens 
                temp = tokens.pop()
            
            if temp == "+" or temp == "-" or temp =="*" or temp == "/":
                stack.append([temp])
            else:
                if len(stack) > 0:
                    stack[-1].append(temp)
                else:
                    break
                
        print(temp)
        return int(temp)
