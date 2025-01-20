class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        num2col: Dict[int, int] = {}
        num2row: Dict[int, int] = {}    
        M, N = len(mat), len(mat[0])
        for row in range(M):
            for col in range(N):
                num = mat[row][col]
                num2row[num] = row
                num2col[num] = col
        
        id2rows: Dict[int, List[bool]] = {row: [False] * N for row in range(M)}
        id2cols: Dict[int, List[bool]] = {col: [False] * M for col in range(N)}
        
        for index, num in enumerate(arr):
            row, col = num2row[num], num2col[num]

            id2rows[row][col] = True
            id2cols[col][row] = True

            if all(id2rows[row]) or all(id2cols[col]):
                return index

