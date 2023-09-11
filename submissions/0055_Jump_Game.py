class Solution:
    def canJump(self, nums: List[int]) -> bool:
        currNum = nums[0]
        
        for i in range(1, len(nums)):
            if currNum == 0:
                return False
            currNum -= 1
            currNum = max(currNum, nums[i])

        return True
