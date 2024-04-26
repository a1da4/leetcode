class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        for rowId in range(1, len(grid)):
            currRow = grid[rowId-1]
            minSum = min(currRow)
            minId = currRow.index(minSum)
            _minSum = min(currRow[:minId] + currRow[minId+1:])
            for colId in range(len(grid[0])):
                if colId == minId:
                    grid[rowId][colId] += _minSum
                else:
                    grid[rowId][colId] += minSum
        return min(grid[-1])
