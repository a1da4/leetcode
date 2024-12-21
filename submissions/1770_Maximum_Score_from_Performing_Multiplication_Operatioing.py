class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        N, M = len(nums), len(multipliers)
        dp = [0] * (M + 1)
        for i in range(M - 1, -1, -1):
            for j in range(0, i + 1, 1):
                dp[j] = max(multipliers[i] * nums[j] + dp[j + 1],
                            multipliers[i] * nums[N - 1 - (i - j)] + dp[j])
            
        return dp[0]

