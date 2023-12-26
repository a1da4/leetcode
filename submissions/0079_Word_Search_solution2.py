class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.matched = False
        numRow = len(board)
        numCol = len(board[0])
        def search(rowId: int, colId: int, word: str):
            if board[rowId][colId] == word[0]:
                if len(word) == 1:
                    self.matched = True
                    return
                char = board[rowId][colId]
                board[rowId][colId] = "."
                if rowId - 1 >= 0:
                    search(rowId - 1, colId, word[1:])
                if rowId + 1 < numRow:
                    search(rowId + 1, colId, word[1:])
                if colId - 1 >= 0:
                    search(rowId, colId - 1, word[1:])
                if colId + 1 < numCol:
                    search(rowId, colId + 1, word[1:])
                board[rowId][colId] = char
        for rowId in range(numRow):
            for colId in range(numCol):
                search(rowId, colId, word)
        
        return self.matched
