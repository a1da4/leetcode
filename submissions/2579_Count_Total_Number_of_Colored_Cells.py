class Solution:
    def coloredCells(self, n: int) -> int:
        answer = 0
        for i in range(n):
            if i == 0:
                answer += 1
            else:
                answer += 4 * i

        return answer
