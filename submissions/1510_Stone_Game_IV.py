class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)
        dp[0] = False
        dp[1] = True

        for i in range(1, n + 1):
            for j in range(1, int(i ** 0.5) + 1):
                if not dp[i - j ** 2]:
                    dp[i] = True
                    break

        return dp[n]

