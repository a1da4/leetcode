class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 1e9 + 7
        dp = [[0] * n for _ in range(5)]
        for i in range(5):
            dp[i][0] = 1
        
        for j in range(1, n):
            dp[0][j] += dp[1][j - 1] % MOD
            dp[1][j] += (dp[0][j - 1] + dp[2][j - 1]) % MOD
            dp[2][j] += (dp[0][j - 1] + dp[1][j - 1] \
                        + dp[3][j - 1] + dp[4][j - 1]) % MOD
            dp[3][j] += (dp[2][j - 1] + dp[4][j - 1]) % MOD
            dp[4][j] += dp[0][j - 1] % MOD
        
        return int(sum([dp[i][n - 1] for i in range(5)]) % MOD)

