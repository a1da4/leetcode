class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        maxSum = -1
        nums.sort()
        for i in range(len(nums)):
            j = bisect_left(nums, k - nums[i], i + 1) - 1
            if j > i:
                maxSum = max(maxSum, nums[i] + nums[j])

        return maxSum

