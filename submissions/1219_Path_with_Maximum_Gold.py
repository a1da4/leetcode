class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        self.answer = 0

        def search(rowId: int, colId: int, currGold: int):
            if rowId < 0 or rowId >= len(grid):
                self.answer = max(self.answer, currGold)
                return
            if colId < 0 or colId >= len(grid[0]):
                self.answer = max(self.answer, currGold)
                return currGold
            if grid[rowId][colId] == 0:
                self.answer = max(self.answer, currGold)
                return currGold

            temp = grid[rowId][colId]
            grid[rowId][colId] = 0
            currGold += temp

            search(rowId + 1, colId, currGold)
            search(rowId - 1, colId, currGold)
            search(rowId, colId + 1, currGold)
            search(rowId, colId - 1, currGold)

            grid[rowId][colId] += temp

        for rowId in range(len(grid)):
            for colId in range(len(grid[0])):
                if grid[rowId][colId] > 0:
                    search(rowId, colId, 0)

        return self.answer

