class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vocab = set(nums)
        for leftId in range(len(nums)):
            rest = target - nums[leftId]
            if rest in vocab:
                rightId = nums.index(rest)
                if rightId != leftId:
                    return [leftId, rightId]
