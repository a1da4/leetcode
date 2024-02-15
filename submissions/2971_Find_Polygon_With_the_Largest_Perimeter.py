class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        currPerim = -1
        N = len(nums)
        currSum = sum(nums)
        for edgeId in range(N-1, 1, -1):
            edgeNum = nums[edgeId]
            currSum -= edgeNum
            if currSum > edgeNum:
                currPerim = max(currPerim, currSum + edgeNum)
        return currPerim
