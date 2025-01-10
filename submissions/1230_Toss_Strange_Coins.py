class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        # 2^len(prob) patterns
        N = len(prob)


        dp = [[0] * (target + 1) for _ in range(N + 1)]
        dp[0][0] = 1

        for i in range(1, N + 1):
            dp[i][0] = dp[i - 1][0] * (1 - prob[i - 1])
            for c in range(1, target + 1):
                if i < c:
                    break
                dp[i][c] = (dp[i - 1][c] * (1 - prob[i - 1]) + dp[i - 1][c - 1] * prob[i - 1])
        
        return dp[N][target]

