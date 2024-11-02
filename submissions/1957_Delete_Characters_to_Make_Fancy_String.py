class Solution:
    def makeFancyString(self, s: str) -> str:
        stack = []
        for ch in s:
            if len(stack) >= 2 and stack[-1] == stack[-2] == ch:
                continue
            stack.append(ch)
        
        return "".join(stack)
    
