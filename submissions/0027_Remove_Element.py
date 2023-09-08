class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        numItems = len(nums)
        numRemoved = 0
        for i in range(numItems):
            if nums[i-numRemoved] == val:
                nums.pop(i-numRemoved)
                numRemoved += 1
        
        return numItems - numRemoved
