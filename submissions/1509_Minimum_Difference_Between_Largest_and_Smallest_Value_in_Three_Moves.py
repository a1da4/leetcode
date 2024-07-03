class Solution:
    def minDifference(self, nums: List[int]) -> int:
        N = len(nums)
        if N <= 4:
            return 0
        
        nums.sort()
        minDiff = float('inf')
        for left in range(4):
            right = N - 4 + left
            minDiff = min(minDiff, nums[right] - nums[left]) 
        
        return minDiff
