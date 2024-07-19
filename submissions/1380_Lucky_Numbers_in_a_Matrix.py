class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        answer = []
        maxCols = set()
        M, N = len(matrix), len(matrix[0])
        for colId in range(N):
            rowId = sorted([(matrix[rowId][colId], rowId) for rowId in range(M)],
                           key=lambda x:x[0], reverse=True)[0][1]
            maxCols.add((rowId, colId))

        for rowId in range(M):
            colId = sorted([(matrix[rowId][colId], colId) for colId in range(N)],
                           key=lambda x:x[0])[0][1]
            if (rowId, colId) in maxCols:
                answer.append(matrix[rowId][colId])
        
        return answer
