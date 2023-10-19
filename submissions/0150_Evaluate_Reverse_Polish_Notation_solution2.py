class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])

        nums = deque()
        opeVocab = set(["+", "-", "*", "/"])
        for token in tokens:
            if token in opeVocab:
                num_0 = nums.pop()
                num_1 = nums.pop()
                if token == "+":
                    num = num_1 + num_0
                elif token == "-":
                    num = num_1 - num_0
                elif token == "*":
                    num = num_1 * num_0
                else:
                    num = num_1 / num_0
                nums.append(int(num))
            else:
                nums.append(int(token))

        return nums.pop()
