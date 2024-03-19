class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numZero = 0
        others = []
        for num in nums:
            if num == 0:
                numZero += 1
            else:
                others.append(num)
        
        nums[:] = others + [0] * numZero
