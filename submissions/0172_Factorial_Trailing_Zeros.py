class Solution:
    def trailingZeroes(self, n: int) -> int:
        currNum = 5
        answer = 0

        while currNum <= n:
            answer += n // currNum
            currNum *= 5

        return answer
