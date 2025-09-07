class Solution:
    def sumZero(self, n: int) -> List[int]:
        answer = []
        if n % 2:
            answer.append(0)
        for i in range(n // 2):
            answer.append(i + 1)
            answer.append(- (i + 1))
        return answer
