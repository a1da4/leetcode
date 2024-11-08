class Solution:
    def minInsertions(self, s: str) -> int:
        
        N = len(s)
        sRev = s[::-1]

        dp = [[0] * (N + 1) for _ in range(N + 1)]

        for i in range(N + 1):
            for j in range(N + 1):
                if i == 0 or j == 0:
                    continue
                elif s[i - 1] == sRev[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j],
                                   dp[i][j - 1])

        return N - dp[N][N]

