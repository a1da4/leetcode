class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 10**9 + 7
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for currRoll in range(n):
            for currId in range(currRoll * 1, currRoll * k + 1):
                for roll in range(1, k+1):
                    if currId + roll > target:
                        continue
                    dp[currRoll + 1][currId + roll] = (dp[currRoll + 1][currId + roll] + dp[currRoll][currId]) % mod

        return dp[-1][-1]
