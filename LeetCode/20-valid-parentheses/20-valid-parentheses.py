class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        
        for p in s:
            if p not in parentheses:
                stack.append(p)
            
            elif not stack or parentheses[p] != stack.pop():
                return False
        
        return len(stack) == 0