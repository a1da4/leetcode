class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowId = 0
        numRow = len(matrix)
        while rowId < numRow and matrix[rowId][-1] < target:
            rowId += 1
        if rowId == numRow:
            return False
        #return target in set(matrix[rowId])
        leftId = 0
        rightId = len(matrix[rowId]) - 1
        while leftId <= rightId:
            midId = (leftId + rightId) // 2
            if matrix[rowId][midId] == target:
                return True
            #elif matrix[rowId][leftId] == target:
            #    return True
            #elif matrix[rowId][rightId] == target:
            #    return True
            elif matrix[rowId][midId] < target:
                leftId = midId + 1
            else:
                rightId = midId - 1
        return False
