class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        numJob = len(jobDifficulty)
        if numJob < d:
            return -1

        dp = [[float("inf")] * numJob for _ in range(d)]
        maxDiff = 0
        currId = 0
        while currId <= numJob - d:
            maxDiff = max(maxDiff, jobDifficulty[currId])
            dp[0][currId] = maxDiff
            currId += 1
        
        currDay = 1
        while currDay < d:
            currTask = currDay
            while currTask <= numJob - d + currDay:
                currDiff = jobDifficulty[currTask]
                result = float("inf")
                backTask = currTask - 1
                while backTask >= currDay - 1:
                    result = min(result, dp[currDay - 1][backTask] + currDiff)
                    currDiff = max(currDiff, jobDifficulty[backTask])
                    backTask -= 1
                dp[currDay][currTask] = result
                currTask += 1
            currDay += 1

        return dp[-1][-1]
