class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        maxEdit = max(len(word1), len(word2))
        editMat = [[0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]

        for rowId in range(len(word1)+1):
            editMat[rowId][0] = rowId
            for colId in range(1, len(word2)+1):
                if rowId == 0:
                    editMat[0][colId] = colId
                elif word1[rowId-1] == word2[colId-1]:
                    editMat[rowId][colId] = editMat[rowId-1][colId-1]
                else:
                    editMat[rowId][colId] = min(editMat[rowId-1][colId-1], editMat[rowId-1][colId], editMat[rowId][colId-1]) + 1

        return editMat[-1][-1]
