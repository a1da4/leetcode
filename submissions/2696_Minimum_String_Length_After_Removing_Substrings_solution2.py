class Solution:
    def minLength(self, s: str) -> int:
        vocab = {"AB", "CD"}
        stack = deque([])
        for ch in s:
            if stack and stack[-1] + ch in vocab:
                stack.pop()
            else:
                stack.append(ch)

        return len(stack)

