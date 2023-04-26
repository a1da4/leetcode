class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # find next permutation
        i = len(nums) - 2

        while i >= 0 and nums[i+1] <= nums[i]:
            i -= 1
        
        if (i >= 0):
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        
        j = len(nums) - 1
        k = i + 1
        # k~j: nums[i+1] <= nums[i]
        while k < j:
            temp = nums[k]
            nums[k] = nums[j]
            nums[j] = temp
            k += 1
            j -= 1
