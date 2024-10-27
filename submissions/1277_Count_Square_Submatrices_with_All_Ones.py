class Solution:
    def _solve(self, 
               rId: int, 
               cId: int, 
               matrix: List[List[int]],
               dp: List[List[int]]) -> int:
        if rId >= len(matrix) or \
            cId >= len(matrix[0]) or \
            matrix[rId][cId] == 0:
            return 0

        if dp[rId][cId] != -1:
            return dp[rId][cId]
        
        dp_r = self._solve(rId, cId + 1, matrix, dp)
        dp_d = self._solve(rId + 1, cId + 1, matrix, dp)
        dp_b = self._solve(rId + 1, cId, matrix, dp)

        dp[rId][cId] = 1 + min(dp_r, min(dp_d, dp_b))

        return dp[rId][cId]

    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[-1] * n for _ in range(m)]
        answer = 0

        for rId in range(m):
            for cId in range(n):
                answer += self._solve(rId, cId, matrix, dp)

        return answer

