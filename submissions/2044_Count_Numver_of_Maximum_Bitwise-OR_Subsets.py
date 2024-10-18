class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxVal = 0
        dp = [0] * (1 << 17)
        dp[0] = 1

        for num in nums:
            for i in range(maxVal, -1, -1):
                dp[i | num] += dp[i]

            maxVal |= num

        return dp[maxVal]
