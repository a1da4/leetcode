class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        currSum = 0
        maxSum = 0
        prev = 0
        for num in nums:
            if prev < num:
                currSum += num
            else:
                maxSum = max(maxSum, currSum)
                currSum = num
            prev = num

        return max(maxSum, currSum)

