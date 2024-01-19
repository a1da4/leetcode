class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        numRow = len(matrix)
        for rowId in range(1, numRow):
            for colId in range(numRow):
                startCol = max(0, colId-1)
                endCol = min(numRow-1, colId+1)
                matrix[rowId][colId] += min(matrix[rowId-1][startCol:endCol+1])
        return min(matrix[-1])
