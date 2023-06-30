class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxSum = currentSum = sum(nums[:k])
        
        for leftId in range(len(nums) - k):
            print(leftId)
            currentSum = currentSum - nums[leftId] + nums[leftId+k]
            maxSum = max(maxSum, currentSum)

        return maxSum / k
