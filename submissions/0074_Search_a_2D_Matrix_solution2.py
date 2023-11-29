class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        targetRowId = 0
        targetColId = 0
        while matrix[targetRowId][-1] < target:
            targetRowId += 1
            if targetRowId >= len(matrix):
                return False

        return target in set(matrix[targetRowId])
