class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if sum(nums) == len(nums):
            return len(nums) - 1

        answer = 0
        curr = 0
        prev = 0
        for num in nums:
            if num == 1:
                curr += 1
            else:
                answer = max(answer, prev + curr)
                prev = curr
                curr = 0

        answer = max(answer, prev + curr)

        return answer
