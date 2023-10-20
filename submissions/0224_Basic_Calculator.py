class Solution:
    def calculate(self, s: str) -> int:
        numVocab = set([str(num) for num in range(10)])
        pmVocab = set(["+", "-"])
        currNum = 0
        result = 0
        is_positive = 1
        stack = deque()
        for char in s:
            if char in numVocab:
                currNum = currNum * 10 + int(char)
            else:
                if char in pmVocab:
                    result += currNum * is_positive
                    is_positive = 1 if char == "+" else -1
                    currNum = 0
                elif char == "(":
                    stack.append(result)
                    stack.append(is_positive)
                    result = 0
                    is_positive = 1
                elif char == ")":
                    result += currNum * is_positive
                    result *= stack.pop()
                    result += stack.pop()
                    currNum = 0

        return result + currNum * is_positive
