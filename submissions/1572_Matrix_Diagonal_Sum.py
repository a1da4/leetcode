class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        answer = 0
        N = len(mat)
        for colId in range(N):
            answer += mat[colId][colId]
            if colId != N - 1 - colId:
                answer += mat[N - 1 - colId][colId]

        return answer

