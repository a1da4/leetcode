class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numId = 0
        numZeros = 0
        while numId < len(nums) - numZeros:
            if nums[numId] == 0:
                nums.pop(numId)
                nums.append(0)
                numZeros += 1
            else:
                numId += 1
