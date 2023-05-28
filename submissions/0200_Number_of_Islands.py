class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def search(grid: List[List[str]], currentRow: int, currentColumn: int):
            stack = [[currentRow, currentColumn]]
            while stack:
                currentRow, currentColumn = stack.pop(0)
                if 0 > currentRow or currentRow >= len(grid):
                    continue
                if 0 > currentColumn or currentColumn >= len(grid[0]):
                    continue
                if grid[currentRow][currentColumn] == "0":
                    continue
                grid[currentRow][currentColumn] = "0"                
                stack.append([currentRow-1, currentColumn])
                stack.append([currentRow+1, currentColumn])
                stack.append([currentRow, currentColumn-1])
                stack.append([currentRow, currentColumn+1])
            
        islandCount = 0
        Row = len(grid)
        Column = len(grid[0])
        for currentRow in range(Row):
            for currentColumn in range(Column):
                if grid[currentRow][currentColumn] == "1":
                    search(grid, currentRow, currentColumn)
                    islandCount += 1
        
        return islandCount
