class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        N = len(coins)
        dp = [[0] * (amount + 1) for _ in range(N + 1)]
        for i in range(N):
            dp[i][0] = 1

        for currCoinId in range(N - 1, -1, -1):
            for currAmount in range(1, amount + 1):
                dp[currCoinId][currAmount] = dp[currCoinId + 1][currAmount]
                if coins[currCoinId] <= currAmount:
                    dp[currCoinId][currAmount] += dp[currCoinId][currAmount - coins[currCoinId]]

        return dp[0][amount]

