class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        leftId = 0
        currentSum = 0
        res = float("inf")

        for rightId in range(len(nums)):
            currentSum += nums[rightId]
            
            while currentSum >= target:
                res = min(res, rightId - leftId + 1)
                currentSum -= nums[leftId]
                leftId += 1
        
        return res if res != float("inf") else 0
