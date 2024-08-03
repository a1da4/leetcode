class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        N = len(costs)
        dp = [[0] * 3 for _ in range(N + 1)]

        for i in range(N):
            cost = costs[i]
            dp[i + 1][0] = min(dp[i][1] + cost[0], dp[i][2] + cost[0])
            dp[i + 1][1] = min(dp[i][0] + cost[1], dp[i][2] + cost[1])
            dp[i + 1][2] = min(dp[i][0] + cost[2], dp[i][1] + cost[2])

        return min(dp[-1])

