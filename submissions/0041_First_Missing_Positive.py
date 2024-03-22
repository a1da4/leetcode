class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        V = set(nums)
        curr = 1
        while curr in V:
            curr += 1
        return curr
