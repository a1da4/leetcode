class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target in set(nums):
            start = nums.index(target)
            end = (len(nums) - 1 - nums[::-1].index(target))
        else:
            start = end = -1

        return [start, end]
