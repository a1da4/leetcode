class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        currentId = 0
        currentNum = nums[currentId]
        while currentNum < target and currentId < len(nums):
            currentId += 1
            if currentId < len(nums):
                currentNum = nums[currentId]
        # break: currentNum >= target or currentId = len(nums)
        targetId = currentId

        return targetId
