class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        targetRowId = 0
        targetColId = 0
        while matrix[targetRowId][-1] < target:
            targetRowId += 1
            if targetRowId >= len(matrix):
                return False

        while matrix[targetRowId][targetColId] < target:
            targetColId += 1
            if targetColId >= len(matrix[0]):
                return False

        return matrix[targetRowId][targetColId] == target
