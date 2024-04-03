class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        numRow, numCol = len(board), len(board[0])
        path = set()

        def dfs(rowId, colId, i):
            if i == len(word):
                return True
            if (rowId < 0 or colId < 0
                or rowId >= numRow or colId >= numCol
                or word[i] != board[rowId][colId]
                or (rowId, colId) in path):
                return False
            path.add((rowId, colId))
            res = (dfs(rowId + 1, colId, i + 1) or dfs(rowId - 1, colId, i + 1)
                    or dfs(rowId, colId + 1, i + 1) or dfs(rowId, colId - 1, i + 1))
            path.remove((rowId, colId))
            return res

        word2freq = sum(map(Counter, board), Counter())
        if word2freq[word[0]] > word2freq[word[-1]]:
            word = word[::-1]

        for rowId in range(numRow):
            for colId in range(numCol):
                if dfs(rowId, colId, 0):
                    return True

        return False

