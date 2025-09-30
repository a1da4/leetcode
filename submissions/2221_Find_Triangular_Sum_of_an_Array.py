class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) > 1:
            _nums = []
            for num1, num2 in zip(nums[:-1], nums[1:]):
                _nums.append((num1 + num2) % 10)
            
            nums = _nums
        
        return nums[0]
