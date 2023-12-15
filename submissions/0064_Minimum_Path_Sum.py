class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        numRow = len(grid)
        numCol = len(grid[0])
        
        for currRow in range(1, numRow):
            grid[currRow][0] += grid[currRow-1][0]
        
        for currCol in range(1, numCol):
            grid[0][currCol] += grid[0][currCol-1]
        
        for currRow in range(1, numRow):
            for currCol in range(1, numCol):
                grid[currRow][currCol] += min(grid[currRow-1][currCol], grid[currRow][currCol-1])
                
        return grid[-1][-1]
