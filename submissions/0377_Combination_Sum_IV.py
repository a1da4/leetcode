class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        N = len(nums)
        nums.sort()

        dp = [0] * (target + 1)
        dp[0] = 1
        
        for currSum in range(target + 1):
            for num in nums:
                if currSum - num >= 0:
                    dp[currSum] += dp[currSum - num]
                else:
                    break

        return dp[target]

