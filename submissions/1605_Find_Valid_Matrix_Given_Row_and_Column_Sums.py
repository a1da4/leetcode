class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        M, N = len(rowSum), len(colSum)

        _rowSum = [0] * M
        _colSum = [0] * N

        matrix = [[0]* N for _ in range(M)]
        for rowId in range(M):
            for colId in range(N):
                matrix[rowId][colId] = min(
                    rowSum[rowId] - _rowSum[rowId],
                    colSum[colId] - _colSum[colId]
                )

                _rowSum[rowId] += matrix[rowId][colId]
                _colSum[colId] += matrix[rowId][colId]

        return matrix

