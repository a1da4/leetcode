class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0
        nums.sort()
        n = 0
        for num in nums:
            if num >= 0:
                break
            else:
                n += 1
        if n%2:
            return -1
        else:
            return 1
        
