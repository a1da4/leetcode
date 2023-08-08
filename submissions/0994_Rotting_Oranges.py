class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        totalTurn = -1
        numRow = len(grid)
        numCol = len(grid[0])

        rottedPositions = deque()
        for i in range(numRow):
            for j in range(numCol):
                if grid[i][j] == 2:
                    rottedPositions.append([i, j])
        
        while rottedPositions:
            numRotted = len(rottedPositions)

            for _ in range(numRotted):
                i, j = rottedPositions.popleft()
                if i - 1 >= 0 and grid[i - 1][j] == 1:
                    rottedPositions.append([i - 1, j])
                    grid[i - 1][j] = 2
                if i + 1 < numRow and grid[i + 1][j] == 1:
                    rottedPositions.append([i + 1, j])
                    grid[i + 1][j] = 2
                if j - 1 >= 0 and grid[i][j - 1] == 1:
                    rottedPositions.append([i, j - 1])
                    grid[i][j - 1] = 2
                if j + 1 < numCol and grid[i][j + 1] == 1:
                    rottedPositions.append([i, j + 1])
                    grid[i][j + 1] = 2
            totalTurn += 1

        for i in range(numRow):
            for j in range(numCol):
                if grid[i][j] == 1:
                    return -1

        if totalTurn == -1:
            return 0
        else:
            return totalTurn
