class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        N = len(stoneValue)
        dp = [0] * (N + 3)

        for i in range(N - 1, -1, -1):
            if i + 2 <= N - 1:
                dp[i] = max(
                    stoneValue[i] - dp[i + 1],
                    stoneValue[i] + stoneValue[i + 1] - dp[i + 2],
                    stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] - dp[i + 3],
                )
            elif i + 1 <= N - 1:
                dp[i] = max(
                    stoneValue[i] - dp[i + 1],
                    stoneValue[i] + stoneValue[i + 1] - dp[i + 2],
                )
            else:
                dp[i] = stoneValue[i] - dp[i + 1]


        if dp[0] > 0:
            return 'Alice'
        elif dp[0] < 0:
            return 'Bob'
        else:
            return 'Tie'

