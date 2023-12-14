class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = [[-1] * len(triangle) for _ in range(len(triangle))]

        def dfs(depthId: int, nodeId: int):
            if depthId == len(triangle):
                return 0
            if memo[depthId][nodeId] != -1:
                return memo[depthId][nodeId]

            lowerLeft = triangle[depthId][nodeId] + dfs(depthId + 1, nodeId)
            lowerRight = triangle[depthId][nodeId] + dfs(depthId + 1, nodeId + 1)
            memo[depthId][nodeId] = min(lowerLeft, lowerRight)
            return memo[depthId][nodeId]

        return dfs(0, 0)
