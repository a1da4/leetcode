class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        answer = 0
        target = max(nums)
        curr = 0
        for num in nums:
            if num == target:
                curr += 1
                answer = max(answer, curr)
            else:
                curr = 0
    
        return answer
