class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for leftId in range(len(nums)):
            rest = target - nums[leftId]
            if rest in nums:
                rightId = nums.index(rest)
                if rightId != leftId:
                    return [leftId, rightId]
