class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]

        for rowId in range(len(matrix)):
            for colId in range(len(matrix[0])):
                if matrix[rowId][colId] == "1":
                    if rowId == 0 or colId == 0:
                        dp[rowId][colId] = 1
                    else:
                        dp[rowId][colId] = min(dp[rowId - 1][colId], 
                                               dp[rowId][colId - 1],
                                               dp[rowId - 1][colId - 1]) + 1
        
        return max([max(row) for row in dp]) ** 2
