class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            targetId = nums.index(target)
        except:
            targetId = -1
        
        return targetId
