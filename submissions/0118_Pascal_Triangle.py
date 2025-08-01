class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = []

        def pascal(curr: List[int]) -> List[int]:
            if len(curr) == 0:
                return [1]
            elif len(curr) == 1:
                return [1, 1]
            else:
                next = []
                for num1, num2 in zip(curr[:-1], curr[1:]):
                    next.append(num1 + num2)

                return [1] + next + [1]

        curr = []
        for i in range(1, numRows + 1):
            curr = pascal(curr)
            answer.append(curr)

        return answer
