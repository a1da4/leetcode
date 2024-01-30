class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        opeVocab = set(["+", "-", "*", "/"])
        for token in tokens:
            if token in opeVocab:
                if token == "+":
                    nums[-2] += nums[-1] 
                elif token == "-":
                    nums[-2] -= nums[-1]
                elif token == "*":
                    nums[-2] *= nums[-1]
                else:
                    nums[-2] = int(nums[-2] / nums[-1])
                nums.pop()
            else:
                nums.append(int(token))

        return nums[-1]
