class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numRow = len(grid)
        numCol = len(grid[0])
        self._answer = 0

        def search(rowId, colId):
            if rowId < 0 or rowId >= numRow or colId < 0 or colId >= numCol:
                return
            if grid[rowId][colId] == "1":
                grid[rowId][colId] = "_"
                search(rowId + 1, colId)
                search(rowId - 1, colId)
                search(rowId, colId + 1)
                search(rowId, colId - 1)
            return

        for rowId in range(numRow):
            for colId in range(numCol):
                if grid[rowId][colId] == "1":
                    self._answer += 1
                    search(rowId, colId)

        return self._answer
