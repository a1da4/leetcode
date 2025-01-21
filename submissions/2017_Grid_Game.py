class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        rowSum0 = sum(grid[0])
        rowSum1 = 0
        minSum = float("inf")
        for downId in range(len(grid[0])):
            rowSum0 -= grid[0][downId]
            minSum = min(minSum, max(rowSum0, rowSum1))
            rowSum1 += grid[1][downId]

        return minSum

