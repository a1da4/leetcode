class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        mod = 10**9 + 7
        N = len(s)
        dp = [1] + [0] * N

        for currId in range(N):
            if s[currId] == "0":
                continue
            count = 0
            for endId in range(currId, N):
                if int(s[currId: endId + 1]) > k:
                    break
                dp[endId + 1] += dp[currId]
                dp[endId + 1] %= mod

        return dp[-1]

