class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        answer = -1
        nums.sort(reverse=True)
        for num in nums:
            if num > 0 and -num in nums:
                return num

        return -1
