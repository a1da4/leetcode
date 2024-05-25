class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        is_moved = True
        M = len(board)
        N = len(board[0])

        def _crush(rowId: int, colId: int, val: int):
            crushIds = [(rowId, colId)]
            if M - 1 - rowId >= 2:
                _rowId = rowId + 1
                _crushIds = []
                while _rowId < M:
                    if board[_rowId][colId] == val:
                        _crushIds.append((_rowId, colId))
                        _rowId += 1
                    else:
                        break
                if len(_crushIds) >= 2:
                    crushIds.extend(_crushIds)

            if N - 1 - colId >= 2:
                _colId = colId + 1
                _crushIds = []
                while _colId < N:
                    if board[rowId][_colId] == val:
                        _crushIds.append((rowId, _colId))
                        _colId += 1
                    else:
                        break
                if len(_crushIds) >= 2:
                    crushIds.extend(_crushIds)

            crushIds = list(set(crushIds))
            return crushIds if len(crushIds) >= 3 else []

        def crush(board):
            is_moved = False
            crush_set = set()
            for rowId in range(M):
                for colId in range(N):
                    if board[rowId][colId] != 0:
                        crushIds = _crush(rowId, colId, board[rowId][colId])
                        if crushIds:
                            crush_set.update(crushIds)

            if crush_set:
                is_moved = True
                for rowId, colId in crush_set:
                    board[rowId][colId] = 0

            return board, is_moved

        def drop(board):
            for colId in range(N):
                rows = [board[rowId][colId] for rowId in range(M) if board[rowId][colId] != 0]
                rows = [0] * (M - len(rows)) + rows
                for rowId in range(M):
                    board[rowId][colId] = rows[rowId]

        while is_moved:
            board, is_moved = crush(board)
            if is_moved:
                drop(board)

        return board

