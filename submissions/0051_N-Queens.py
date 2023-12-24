class Solution:
    def solveNQueens(self, n: int) -> int:
        self.answer = []
        def isSafe(rowId: int, colId: int, board: List[List[str]]) -> bool:
            _rowId, _colId = rowId, colId
            while _rowId >= 0 and _colId >= 0:
                if board[_rowId][_colId] == "Q":
                    return False
                _rowId -= 1
                _colId -= 1 
            _rowId, _colId = rowId, colId
            while _rowId < n and _colId >= 0:
                if board[_rowId][_colId] == "Q":
                    return False
                _rowId += 1
                _colId -= 1
            while colId >= 0:
                if board[rowId][colId] == "Q":
                    return False
                colId -= 1
            return True
        
        def search(colId: int, board: List[List[str]]) -> None:
            #nonlocal answer
            if colId == n:
                self.answer.append([col for col in board])
                return
            for rowId in range(n):
                if isSafe(rowId, colId, board):
                    board[rowId] = board[rowId][:colId] + "Q" + board[rowId][colId+1:]
                    search(colId + 1, board)
                    board[rowId] = board[rowId][:colId] + "." + board[rowId][colId+1:]

        board = ["." * n for _ in range(n)]
        search(0, board)
        return self.answer
