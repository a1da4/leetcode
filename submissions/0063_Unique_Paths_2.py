class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        numDownToGo = len(obstacleGrid) - 1
        numRightToGo = len(obstacleGrid[0]) - 1
        
        @cache
        def depthFirstSearch(downId, rightId):
            if obstacleGrid[downId][rightId]:
                return 0
            if downId == numDownToGo and rightId == numRightToGo:
                return 1
            
            totalPathes = 0

            if downId < numDownToGo:
                totalPathes += depthFirstSearch(downId + 1, rightId)
            if rightId < numRightToGo:
                totalPathes += depthFirstSearch(downId, rightId + 1)
            
            return totalPathes
        
        return depthFirstSearch(0, 0)
