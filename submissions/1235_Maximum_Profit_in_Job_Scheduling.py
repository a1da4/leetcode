class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        numJob = len(startTime)
        dp = [0] * numJob
        sortedJob = sorted(zip(startTime, endTime, profit), key=lambda x:x[1])
        sortedEndTime = [job[1] for job in sortedJob]
        dp[0] = sortedJob[0][2]

        for currJob in range(1, numJob):
            startDay, _, currProfit = sortedJob[currJob]
            endId = bisect.bisect_right(sortedEndTime, startDay) - 1
            if endId >= 0:
                currProfit += dp[endId]
            dp[currJob] = max(currProfit, dp[currJob - 1])

        return dp[-1]
