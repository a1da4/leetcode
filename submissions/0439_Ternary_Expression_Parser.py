class Solution:
    def parseTernary(self, expression: str) -> str:
        stack = []
        for ch in expression[::-1]:
            if stack and stack[-1] == "?":
                stack.pop()
                valTrue = stack.pop()
                stack.pop()
                valFalse = stack.pop()
                stack.append(valTrue if ch == "T" else valFalse)
            else:
                stack.append(ch)
        return stack[0]
