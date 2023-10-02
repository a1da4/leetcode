class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        results = []
        for rowId in range(9):
            for colId in range(9):
                target = board[rowId][colId]
                if target == '.':
                    continue
                results += [(rowId, target), (target, colId), (rowId//3, colId//3, target)]
        return len(results) == len(set(results))
