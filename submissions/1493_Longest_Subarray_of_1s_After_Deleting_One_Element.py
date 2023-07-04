class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        leftId = 0
        numDel = 1

        for rightId in range(len(nums)):
            if nums[rightId] == 0:
                numDel -= 1
            if numDel < 0:
                if nums[leftId] == 0:
                    numDel += 1
                leftId += 1
        
        return rightId - leftId
