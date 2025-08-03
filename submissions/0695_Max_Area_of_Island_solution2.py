class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        answer = 0
        R, C = len(grid), len(grid[0])
        self.currArea = 0

        def searchIsland(row: int, col: int):
            if grid[row][col] == 0:
                return
            self.currArea += 1
            grid[row][col] = 0
            if row + 1 < R:
                searchIsland(row + 1, col)
            if row - 1 >= 0:
                searchIsland(row - 1, col)
            if col + 1 < C:
                searchIsland(row, col + 1)
            if col - 1 >= 0:
                searchIsland(row, col - 1)

        for r in range(R):
            for c in range(C):
                if grid[r][c]:
                    self.currArea = 0
                    searchIsland(r, c)
                    answer = max(
                        answer,
                        self.currArea,
                    )
        return answer
