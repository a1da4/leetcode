class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        for rowId in range(1, len(grid)):
            currRow = deque(grid[rowId-1])
            for colId in range(len(grid[0])):
                currRow.popleft()
                grid[rowId][colId] += min(currRow)
                currRow.append(grid[rowId-1][colId])

        return min(grid[-1])
