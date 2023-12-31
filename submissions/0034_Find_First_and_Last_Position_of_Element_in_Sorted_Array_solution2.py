class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        leftId = 0
        rightId = len(nums) - 1
        while leftId <= rightId:
            midId = (leftId + rightId) // 2
            if nums[midId] < target:
                leftId = midId + 1
            elif nums[midId] > target:
                rightId = midId - 1
            else:
                if nums[leftId] == nums[rightId] == target:
                    return [leftId, rightId]
                elif nums[leftId] < target:
                    leftId += 1
                else:
                    rightId -= 1
        return [-1, -1]
