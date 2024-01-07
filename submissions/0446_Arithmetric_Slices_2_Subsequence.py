class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        N = len(nums)
        totalCount = 0  
        dp = [defaultdict(int) for _ in range(N)]

        for i in range(1, N):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += 1  
                if diff in dp[j]:
                    dp[i][diff] += dp[j][diff]
                    totalCount += dp[j][diff]

        return totalCount
