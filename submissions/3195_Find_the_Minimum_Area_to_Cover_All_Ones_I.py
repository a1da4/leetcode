class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        topRow, bottomRow = R - 1, 0
        leftCol, rightCol = C - 1, 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    topRow = min(r, topRow)
                    bottomRow = max(r, bottomRow)
                    leftCol = min(c, leftCol)
                    rightCol = max(c, rightCol)

        return (bottomRow - topRow + 1) * (rightCol - leftCol + 1)

