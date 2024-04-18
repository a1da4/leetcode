class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # check (i+1, j), (i-1, j), (i, j+1), (i, j-1)
        # 
        def check(rowId: int, colId: int) -> int:
            if rowId < 0 or rowId >= len(grid):
                return 0
            if colId < 0 or colId >= len(grid[0]):
                return 0
            return grid[rowId][colId]

        answer = 0
        for rowId in range(len(grid)):
            for colId in range(len(grid[0])):
                if grid[rowId][colId]:
                    answer += 4 - (check(rowId + 1, colId) + \
                                check(rowId - 1, colId) + \
                                check(rowId, colId + 1) + \
                                check(rowId, colId - 1))

        return answer
