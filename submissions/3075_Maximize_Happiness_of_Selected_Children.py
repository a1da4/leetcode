class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        answer = 0
        for curr in range(k):
            answer += max(happiness[-(1 + curr)] - curr, 0)

        return answer

