class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums.sort()
        numDeleted = 0
        numItems = len(nums)
        currNum = nums[0]
        currFreq = 0
        for i in range(numItems):
            num = nums[i - numDeleted]
            if currNum == num:
                currFreq += 1
                if currFreq > 2:
                    nums.pop(i - numDeleted)
                    numDeleted += 1
            else:
                currNum = num
                currFreq = 1
        
        return len(nums)
