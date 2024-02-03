class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        answer = []
        N = len(arr)

        dp = [0] * (k + 1)

        for startId in range(N - 1, -1, -1):
            currMax = 0
            endId = min(N, startId + k)
            for currId in range(startId, endId):
                currMax = max(currMax, arr[currId])
                dp[startId % (k + 1)] = max(dp[startId % (k + 1)], 
                    dp[(currId + 1) % (k + 1)] + currMax * (currId - startId + 1))

        return dp[0]
