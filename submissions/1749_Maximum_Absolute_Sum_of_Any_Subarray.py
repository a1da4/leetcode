class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        curr_sum = 0
        max_sum = - float("inf")
        for num in nums:
            curr_sum = max(curr_sum + num, num)
            max_sum = max(max_sum, curr_sum)

        curr_sum = 0
        min_sum = float("inf")
        for num in nums:
            curr_sum = min(curr_sum + num, num)
            min_sum = min(min_sum, curr_sum)

        best_sum = max(max_sum, abs(min_sum))
        return best_sum

