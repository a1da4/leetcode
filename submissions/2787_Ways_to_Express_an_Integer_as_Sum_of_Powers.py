class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        mod = 10 ** 9 + 7

        nums = []
        curr = 1
        while curr ** x <= n:
            nums.append(curr ** x)
            curr += 1

        m = len(nums)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        dp[0][0] += 1

        for i in range(1, m + 1):
            power = nums[i - 1]
            for k in range(n + 1):
                dp[i][k] = dp[i - 1][k]
                if k >= power:
                    dp[i][k] = (dp[i][k] + dp[i - 1][k - power]) % mod

        return dp[m][n]

