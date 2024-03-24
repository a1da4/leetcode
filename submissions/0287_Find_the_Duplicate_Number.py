class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        founds = set()
        for num in nums:
            if num in founds:
                return num
            else:
                founds.add(num)
