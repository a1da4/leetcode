class Solution:
    def maxScoreSightseeingPair(self, values):
        N = len(values)
        lScores = [0] * N
        lScores[0] = values[0]
        answer = 0

        for i in range(1, N):
            rScore = values[i] - i
            answer = max(answer, lScores[i - 1] + rScore)
            lScore = values[i] + i
            lScores[i] = max(lScores[i - 1], lScore)

        return answer

