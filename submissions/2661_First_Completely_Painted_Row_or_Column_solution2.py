class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        M, N = len(mat), len(mat[0])
        num2row: Dict[int, int] = {}    
        num2col: Dict[int, int] = {}        
        for row in range(M):
            for col in range(N):
                num = mat[row][col]
                num2row[num] = row
                num2col[num] = col
        
        id2rows: Dict[int, int] = {row: 0 for row in range(M)}
        id2cols: Dict[int, int] = {col: 0 for col in range(N)}
        
        for index, num in enumerate(arr):
            row, col = num2row[num], num2col[num]

            id2rows[row] += 1
            id2cols[col] += 1

            if id2rows[row] == N or id2cols[col] == M:
                return index

