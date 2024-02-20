class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        N = len(nums)
        for currId, num in enumerate(sorted(nums)):
            if currId != num:
                return currId
        
        return N
