class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        avoidIds = set()
        numRows = len(board)
        numCols = len(board[0])

        def dfs(rowId: int, colId: int):
            if rowId < 0 or numRows <= rowId:
                return
            if colId < 0 or numCols <= colId:
                return
            if board[rowId][colId] == "X":
                return
            if (rowId, colId) in avoidIds:
                return
            
            avoidIds.add((rowId, colId))
            dfs(rowId, colId + 1)
            dfs(rowId, colId - 1)
            dfs(rowId + 1, colId)
            dfs(rowId - 1, colId)

        for rowId in range(numRows):
            dfs(rowId, 0)
            dfs(rowId, numCols - 1)
        
        for colId in range(numCols):
            dfs(0, colId)
            dfs(numRows - 1, colId)
        
        for rowId in range(numRows):
            for colId in range(numCols):
                if board[rowId][colId] == "O" and (rowId, colId) not in avoidIds:
                    board[rowId][colId] = "X"
