class Solution:
    def isValid(self, s: str) -> bool:
        rev = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        
        stack = []
        for c in s:
            if c in rev:
                top = stack.pop() if stack else "-"
                if rev[c] != top:
                    return False
            else:
                stack.append(c)
        return len(stack)==0