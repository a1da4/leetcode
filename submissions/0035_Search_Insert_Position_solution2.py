class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        N = len(nums)
        leftId = 0
        rightId = N - 1
        while leftId <= rightId:
            midId = (leftId + rightId) // 2
            if nums[midId] == target:
                return midId
            elif nums[midId] > target:
                rightId = midId - 1
            else:
                leftId = midId + 1
        return leftId
