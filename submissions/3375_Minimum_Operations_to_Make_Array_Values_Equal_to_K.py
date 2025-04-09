class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        minNum, maxNum = min(nums), max(nums)
        if minNum < k:
            return -1

        return len(set(nums)) - (k in nums)

