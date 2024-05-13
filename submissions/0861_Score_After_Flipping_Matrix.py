class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        numRow = len(grid)
        numCol = len(grid[0])

        for colId in range(numCol):
            if colId == 0:
                for rowId in range(numRow):
                    if grid[rowId][colId] == 0:
                        for _colId in range(numCol):
                            grid[rowId][_colId] = 1 - grid[rowId][_colId]
            else:
                col = [grid[rowId][colId] for rowId in range(numRow)]
                _col = [1 - val for val in col]
                if sum(col) < sum(_col):
                    for _rowId in range(numRow):
                        grid[_rowId][colId] = 1 - grid[_rowId][colId]

        return sum([sum([val * 2 ** digit for digit, val in enumerate(row[::-1])]) for row in grid])
