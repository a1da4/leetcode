class Solution:
    def findPermutation(self, s: str) -> List[int]:
        answer = []
        stack = []
        for n_1, label in enumerate(s):
            stack.append(n_1 + 1)
            if label == 'I':
                while stack:
                    answer.append(stack.pop())
        stack.append(len(s) + 1)
        while stack:
            answer.append(stack.pop())

        return answer
