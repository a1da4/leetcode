class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid) - 1
        n = len(obstacleGrid[0]) - 1

        memo = {}        
        def dfs(downId, rightId):
            if (downId, rightId) in memo:
                return memo[(downId, rightId)]
            if obstacleGrid[downId][rightId]:
                return 0
            if downId == m and rightId == n:
                return 1
            
            totalPathes = 0

            if downId < m:
                totalPathes += dfs(downId + 1, rightId)
            if rightId < n:
                totalPathes += dfs(downId, rightId + 1)
            
            memo[(downId, rightId)] = totalPathes
            
            return totalPathes
        
        return dfs(0, 0)
