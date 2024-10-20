class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = deque()
        for ch in expression:
            if ch == ")":
                vals = []
                while stack and stack[-1] != "(":
                    vals.append(stack.pop())
                stack.pop()

                operation = stack.pop()

                result = self.evaluateBoolExpr(operation, vals)
                stack.append(result)

            elif ch != ",":
                stack.append(ch)

        return stack[-1] == "t"


    def evaluateBoolExpr(self, operation: str, vals: List[str]) -> str:
        if operation == "!":
            return "f" if vals[0] == "t" else "t"
        
        if operation == "&":
            for val in vals:
                if val == "f":
                    return "f"
            return "t"
        
        if operation == "|":
            for val in vals:
                if val == "t":
                    return "t"
            return "f"

