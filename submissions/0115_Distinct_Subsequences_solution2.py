class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        ns, nt = len(s), len(t)
        dp = [[0] * (nt + 1) for _ in range(ns + 1)]

        for i in range(ns + 1):
            dp[i][nt] = 1

        for sId in range(ns - 1, -1, -1):
            for tId in range(nt - 1, -1, -1):
                dp[sId][tId] = dp[sId + 1][tId]
                
                if s[sId] == t[tId]:
                    dp[sId][tId] += dp[sId + 1][tId + 1]

        return dp[0][0]

