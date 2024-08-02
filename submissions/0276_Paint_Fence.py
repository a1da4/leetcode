class Solution:
    def numWays(self, n: int, k: int) -> int:
        memo = {1: k, 2: k ** 2}
        def dp(num: int):
            if num in memo:
                return memo[num]
            memo[num] = (k - 1) * (dp(num - 1) + dp(num - 2))
            return memo[num]

        return dp(n)

