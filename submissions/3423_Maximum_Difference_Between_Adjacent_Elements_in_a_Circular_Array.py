class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        answer = 0
        for i in range(len(nums)):
            if i == len(nums) - 1:
                answer = max(answer, abs(nums[0] - nums[i]))
            else:
                answer = max(answer, abs(nums[i] - nums[i + 1]))
        
        return answer
