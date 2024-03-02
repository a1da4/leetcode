class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return [(num)**2 for num in sorted([abs(num) for num in nums])]
