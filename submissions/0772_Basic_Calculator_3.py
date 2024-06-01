class Solution:
    def calculate(self, s: str) -> int:
        def evaluate(operator, x, y = 0):
            if operator == "+":
                return x
            if operator == "-":
                return -x
            if operator == "*":
                return x * y
            return int(x / y)

        s += "@"
        N = len(s)

        def _calculate(currId: int, is_paren: bool = False) -> int:
            stack = []
            curr = 0
            is_finish = False
            previous_operator = "+"
            
            while currId < N:
                if s[currId] == "(":
                    curr, currId = _calculate(currId + 1, True)
                elif s[currId] == ")":
                    is_finish = True
                    if previous_operator in "*/":
                        stack.append(evaluate(previous_operator, stack.pop(), curr))
                    else:
                        stack.append(evaluate(previous_operator, curr))
                elif s[currId].isdigit():
                    curr = curr * 10 + int(s[currId])
                else:
                    if previous_operator in "*/":
                        stack.append(evaluate(previous_operator, stack.pop(), curr))
                    else:
                        stack.append(evaluate(previous_operator, curr))        
                    curr = 0
                    previous_operator = s[currId]
                if is_paren and is_finish:
                    break
                currId += 1

            if is_paren:
                return sum(stack), currId
            else:
                return sum(stack)
        
        return _calculate(0)
