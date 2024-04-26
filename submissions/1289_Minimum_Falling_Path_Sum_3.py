class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        for rowId in range(1, len(grid)):
            for colId in range(len(grid[0])):
                grid[rowId][colId] += min(grid[rowId-1][:colId] + grid[rowId-1][colId+1:])

        return min(grid[-1])
