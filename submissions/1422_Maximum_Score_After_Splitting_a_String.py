class Solution:
    def maxScore(self, s: str) -> int:
        left = 1 if s[0] == "0" else 0
        right = s[1:].count("1")
        score = left + right
        N = len(s)

        for currId in range(1, N - 1):
            if s[currId] == "0":
                left += 1
            else:
                right -= 1
            
            score = max(score, left + right)

        return score

