class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in set(nums):
            return -1
        else:
            return nums.index(target)
