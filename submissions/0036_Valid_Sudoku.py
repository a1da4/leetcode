class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # check 3*3 matrix
        def checkMatrix(board: List[List[str]]) -> bool:
            ranges = [[0, 2], [3, 5], [6, 8]]
            for rowIds in ranges:
                for colIds in ranges:
                    items = [board[i][j] for i in range(rowIds[0], rowIds[1] + 1) for j in range(colIds[0], colIds[1] + 1)]
                    item2freq = Counter(items)
                    for num in range(1, 10):
                        strNum = str(num)
                        if strNum in item2freq and item2freq[strNum] > 1:
                            return False
            return True

        # check row & column
        def checkRowColumn(rowId: int, colId: int, target: str, board: List[List[str]]) -> bool:
            for index in range(9):
                if index != rowId and board[index][colId] == target:
                    return False
                if index != colId and board[rowId][index] == target:
                    return False
            return True

        if checkMatrix(board) is False:
            return False
        for rowId in range(9):
            for colId in range(9):
                if board[rowId][colId] == ".":
                    continue
                if checkRowColumn(rowId, colId, board[rowId][colId], board) is False:
                    return False
        return True
