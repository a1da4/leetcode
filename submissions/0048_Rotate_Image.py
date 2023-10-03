class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        _mat = copy.deepcopy(matrix)

        for colId in range(n):
            row = _mat[n - colId - 1]
            for rowId, item in enumerate(row):
                matrix[rowId][colId] = item
