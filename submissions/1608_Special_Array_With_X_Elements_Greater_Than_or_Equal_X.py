class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for x in range(len(nums) + 1):
            rank = sum([1 if num >= x else 0 for num in nums])
            if rank == x:
                return x
        return -1

