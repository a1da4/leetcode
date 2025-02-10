class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        numbers = {'1', '2', '3', '4', '5',
                   '6', '7', '8', '9', '0'} 
        for ch in s:
            if ch in numbers:
                if stack and stack[-1] not in numbers:
                    stack.pop()
                continue
            else:
                stack.append(ch)

        return "".join(stack)

