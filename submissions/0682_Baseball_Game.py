class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for command in operations:
            if command == "C":
                if stack:
                    stack.pop()
            elif command == "D":
                if stack:
                    stack.append(stack[-1] * 2)
            elif command == "+":
                if len(stack) >= 2:
                    stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(command))

        return sum(stack)
