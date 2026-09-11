class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        c2p = {')': '(', "]" : '[', "}" : '{' }
        for c in s:
            if c in c2p:
                if stack and stack[-1] == c2p[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0

        
                 