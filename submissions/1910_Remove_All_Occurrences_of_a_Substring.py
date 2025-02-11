class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        L = len(part)
        for ch in s:
            stack.append(ch)
            while stack and len(stack) >= L and ''.join(stack[-L:]) == part:
                for _ in range(L):
                    stack.pop()

        return ''.join(stack)

