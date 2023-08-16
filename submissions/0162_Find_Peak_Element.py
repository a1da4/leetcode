class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        sortedNums = sorted([(num, index) for index, num in enumerate(nums)])
        return sortedNums[-1][1]
