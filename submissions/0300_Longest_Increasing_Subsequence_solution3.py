class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        numDp = 0
        for num in nums:
            insertId = bisect.bisect_left(dp, num)
            if insertId == len(dp):
                dp.append(num)
                numDp += 1
            else:
                dp[insertId] = num
        
        return numDp
