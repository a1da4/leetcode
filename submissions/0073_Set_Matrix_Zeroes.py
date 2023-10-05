class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        _matrix = copy.deepcopy(matrix)
        for rowId in range(len(matrix)):
            if all(_matrix[rowId]):
                continue
            else:
                matrix[rowId][:] = [0] * len(matrix[0])
        
        for colId in range(len(matrix[0])):
            if all([_matrix[rowId][colId] for rowId in range(len(matrix))]):
                continue
            else:
                for rowId in range(len(matrix)):
                    matrix[rowId][colId] = 0
        
