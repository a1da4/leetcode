class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [1] * (N)
        for rightId in range(N):
            for leftId in range(rightId):
                if nums[leftId] < nums[rightId] and dp[leftId] + 1 > dp[rightId]:
                    dp[rightId] = dp[leftId] + 1
        return max(dp)
