class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        leftSum = 0
        rightSum = sum(nums[1:])

        if leftSum == rightSum:
            return 0
        
        for currentId in range(1, len(nums)):
            leftSum += nums[currentId-1]
            rightSum -= nums[currentId]

            if leftSum == rightSum:
                return currentId

        return -1
