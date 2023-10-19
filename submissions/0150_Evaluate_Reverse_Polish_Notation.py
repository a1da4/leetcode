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
                nums.append(int(eval(str(num_1)+token+str(num_0))))
            else:
                nums.append(int(token))

        return nums.pop()

