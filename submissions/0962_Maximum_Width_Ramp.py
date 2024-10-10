class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        answer = 0
        stack = deque([])
        for i, num in enumerate(nums):
            if not stack or nums[stack[-1]] > num:
                stack.append(i)
        
        for j in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[j]:
                answer = max(answer, j - stack[-1])
                stack.pop()
        
        return answer

