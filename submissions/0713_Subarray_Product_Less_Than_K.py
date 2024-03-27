class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        answer = 0
        curr = 1
        leftId = 0
        for rightId, num in enumerate(nums):
            curr *= num
            while leftId <= rightId and curr >= k:
                curr //= nums[leftId]
                leftId += 1
            answer += rightId - leftId + 1
            
        return answer

