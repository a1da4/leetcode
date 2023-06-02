class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [1 for _ in range(N)]
        for rightId in range(N):
            for leftId in range(rightId):
                if nums[leftId] < nums[rightId] and dp[rightId] < dp[leftId] + 1:
                    dp[rightId] = dp[leftId] + 1
        
        return max(dp)
