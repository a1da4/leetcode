class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def kadane(nums: List[int]) -> int:
            maxSum = currSum = nums[0]
            for num in nums[1:]:
                currSum = max(num, currSum + num)
                maxSum = max(maxSum, currSum)
            return maxSum
        
        maxSum = kadane(nums)
        minSum = kadane([-num for num in nums])
        totalSum = sum(nums)

        return max(maxSum, totalSum + minSum) if maxSum > 0 else maxSum
