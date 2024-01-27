class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dp = defaultdict(int)
        
        def dfs(rowId: int, colId: int, numMove: int):
            if rowId < 0 or rowId >= m or colId < 0 or colId >= n:
                return 1
            
            if (rowId, colId, numMove) in dp:
                return dp[(rowId, colId, numMove)]
            
            if numMove > 0:
                dp[(rowId, colId, numMove)] = dfs(rowId + 1, colId, numMove - 1) \
                + dfs(rowId - 1, colId, numMove - 1) \
                + dfs(rowId, colId + 1, numMove - 1) \
                + dfs(rowId, colId - 1, numMove - 1)
                return dp[(rowId, colId, numMove)]
            else:
                return 0
        
        return dfs(startRow, startColumn, maxMove) % (10**9 + 7)
