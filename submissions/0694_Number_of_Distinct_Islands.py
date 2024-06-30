class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])

        def search(rowId, colId):
            grid[rowId][colId] = 2
            currIsland.add((rowId - _rowId, colId - _colId))
            if rowId + 1 < R and grid[rowId + 1][colId] == 1:
                search(rowId + 1, colId)
            if rowId - 1 >= 0 and grid[rowId - 1][colId] == 1:
                search(rowId - 1, colId)
            if colId + 1 < C and grid[rowId][colId + 1] == 1:
                search(rowId, colId + 1)
            if colId - 1 >= 0 and grid[rowId][colId - 1] == 1:
                search(rowId, colId - 1)

        islands = set()
        for rowId in range(R):
            for colId in range(C):
                if grid[rowId][colId] == 1:
                    currIsland = set()
                    _rowId = rowId
                    _colId = colId
                    search(rowId, colId)
                    if currIsland:
                        islands.add(frozenset(currIsland))

        return len(islands)

