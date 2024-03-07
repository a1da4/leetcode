class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        numRow = len(matrix)
        numCol = len(matrix[0])
        rowIds = set()
        colIds = set()
        for rowId in range(numRow):
            for colId in range(numCol):
                if matrix[rowId][colId] == 0:
                    if rowId not in rowIds:
                        rowIds.add(rowId)
                    if colId not in colIds:
                        colIds.add(colId)
        
        for rowId in list(rowIds):
            matrix[rowId][:] = [0] * numCol
        
        for colId in list(colIds):
            for rowId in range(numRow):
                matrix[rowId][colId] = 0
        
