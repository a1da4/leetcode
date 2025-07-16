class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        nums = [num % 2 for num in nums]

        nZero, nOne = 0, 0
        for num in nums:
            if nZero % 2 and num == 0:
                nZero += 1
            elif nZero % 2 == 0 and num == 1:
                nZero += 1

            if nOne % 2 and num == 1:
                nOne += 1
            elif nOne % 2 == 0 and num == 0:
                nOne += 1
    
        return max(sum(nums), len(nums) - sum(nums), nZero, nOne)

