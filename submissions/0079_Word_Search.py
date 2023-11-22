class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        root = {}
        node = root
        for char in word:
            node[char] = {}
            node = node[char]
        node["end"] = word
        self._matched = False

        def search(rowId: int, colId: int, node):
            if rowId < 0 or rowId >= len(board):
                return
            if colId < 0 or colId >= len(board[0]):
                return
            
            char = board[rowId][colId]
            if char in node:
                node = node[char]
                if "end" in node:
                    self._matched = True
                    return
                board[rowId][colId] = "_"
                search(rowId + 1, colId, node)
                search(rowId - 1, colId, node)
                search(rowId, colId + 1, node)
                search(rowId, colId - 1, node)
                board[rowId][colId] = char
        
        for rowId in range(len(board)):
            for colId in range(len(board[0])):
                if board[rowId][colId] == word[0]:
                    search(rowId, colId, root)
                    if self._matched:
                        return True
        return False
