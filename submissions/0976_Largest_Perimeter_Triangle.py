class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        
        for leftId in range(len(nums) - 2):
            left, center, right = nums[leftId], nums[leftId+1], nums[leftId+2]
            if left < center + right:
                return left + center + right

        return 0

