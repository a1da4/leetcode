class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        M, N = len(grid), len(grid[0])
        mod = 10**9 + 7
        memo = {}

        def travel(rowId: int, colId: int) -> int:
            if (rowId, colId) in memo:
                return memo[(rowId, colId)]
            
            numPaths = 1

            for dr, dc in directions:
                nextRowId, nextColId = rowId + dr, colId + dc
                if 0 <= nextRowId < M \
                    and 0 <= nextColId < N \
                    and grid[rowId][colId] < grid[nextRowId][nextColId]:
                    numPaths += travel(nextRowId, nextColId)
                    numPaths %= mod

            memo[(rowId, colId)] = numPaths
            return numPaths

        answer = 0
        for rowId in range(M):
            for colId in range(N):
                answer += travel(rowId, colId)
                answer %= mod

        return answer

