class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        leftId = 0

        for rightId in range(len(nums)):
            if nums[rightId] == 0:
                k -= 1
            if k < 0:
                if nums[leftId] == 0:
                    k += 1
                leftId += 1
        
        return rightId - leftId + 1
