class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = deque([])
        for ch in s:
            if stack and stack[-1] == "(" and ch == ")":
                stack.pop()
            else:
                stack.append(ch)
        return len(stack)

