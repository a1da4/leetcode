class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane algorithm
        currentSum = nums[0]
        maxSum = currentSum
        if len(nums) == 1:
            return maxSum
        
        for num in nums[1:]:
            currentSum = max(currentSum + num, num)
            maxSum = max(maxSum, currentSum)
            
        return maxSum
