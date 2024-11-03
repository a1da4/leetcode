class Solution:
    def minimumTotalDistance(self, robot, factory):
        robot.sort()
        factory.sort(key=lambda x: x[0])

        fPositions = []
        for x, l in factory:
            for _ in range(l):
                fPositions.append(x)

        numR, numF = len(robot), len(fPositions)
        dp = [[0] * (numF + 1) for _ in range(numR + 1)]

        for i in range(numR):
            dp[i][numF] = float("inf")

        for i in range(numR - 1, -1, -1):
            for j in range(numF - 1, -1, -1):
                dp[i][j] = min(dp[i][j+1],
                    abs(robot[i] - fPositions[j]) + dp[i+1][j+1])

        return dp[0][0]

