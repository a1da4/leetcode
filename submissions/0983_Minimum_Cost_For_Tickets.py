class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * (days[-1] + 1)
        
        curr = 0
        for day in range(1, days[-1] + 1):
            if day < days[curr]:
                dp[day] = dp[day - 1]
            else:
                curr += 1
                dp[day] = min(dp[day - 1] + costs[0],
                              dp[max(0, day - 7)] + costs[1],
                              dp[max(0, day - 30)] + costs[2])
        return dp[-1]

