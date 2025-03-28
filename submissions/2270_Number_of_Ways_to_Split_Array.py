class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        answer = 0
        left, right = 0, sum(nums)

        for i in range(len(nums) - 1):
            left += nums[i]
            right -= nums[i]
            if left >= right:
                answer += 1

        return answer

