class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        N = len(nums)
        target = sum(nums) // 2
        if target * 2 != sum(nums):
            return False

        dp = set()
        dp.add(0)
        dp.add(nums[-1])

        for currId in range(N - 2, -1, -1):
            currDp = set()
            for contextNum in dp:
                currDp.add(contextNum + nums[currId])
            dp.update(currDp)

        return target in dp
