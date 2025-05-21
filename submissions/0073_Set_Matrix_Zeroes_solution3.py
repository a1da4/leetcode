class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeroIds = set()
        R, C = len(matrix), len(matrix[0])
        for row in range(R):
            for col in range(C):
                if matrix[row][col] == 0:
                    for r in range(R):
                        zeroIds.add((r, col))
                    for c in range(C):
                        zeroIds.add((row, c))
        
        for zeroId in list(zeroIds):
            matrix[zeroId[0]][zeroId[1]] = 0

