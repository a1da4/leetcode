class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        totalSum = sum(nums)
        if totalSum < target:
            return 0

        dp = [0] * (2 * totalSum + 1)
        dp[totalSum + nums[0]] = 1
        dp[totalSum - nums[0]] += 1

        for currId in range(1, len(nums)):
            currNum = nums[currId]
            nextDp = [0] * (2 * totalSum + 1)
            for currSum in range(-totalSum, totalSum + 1):
                if dp[currSum + totalSum] > 0:
                    nextDp[currNum + currSum + totalSum] += dp[
                        currSum + totalSum
                    ]
                    nextDp[-currNum + currSum + totalSum] += dp[
                        currSum + totalSum
                    ]
            dp = nextDp

        return dp[target + totalSum]
        
