class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        @cache
        def helper(fromRow: int, toRow: int, fromCol: int, toCol: int):
            loRow, loCol = float('inf'), float('inf')
            hiRow, hiCol = -float('inf'), -float('inf')
            for r in range(fromRow, toRow + 1):
                for c in range(fromCol, toCol + 1):
                    if grid[r][c] == 1:
                        loRow, loCol = min(loRow, r), min(loCol, c)
                        hiRow, hiCol = max(hiRow, r), max(hiCol, c)

            return (hiRow - loRow + 1) * (hiCol - loCol + 1)

        m = len(grid)
        n = len(grid[0])
        res = m * n

        for i in range(m - 1):
            for j in range(i + 1, m - 1):
                res = min(
                    helper(0, i, 0, n - 1) + helper(i + 1, j, 0, n-1) + helper(j + 1, m - 1, 0, n - 1),
                    res,
                )

        for i in range(n - 1):
            for j in range(i + 1, n - 1):
                res = min(
                    helper(0, m - 1, 0, i) + helper(0, m - 1, i + 1, j) + helper(0, m - 1, j + 1, n - 1),
                    res,
                )
        
        for i in range(m - 1):
            for j in range(n - 1):
                res = min(
                    helper(0, i, 0, n - 1) + helper(i + 1, m - 1, 0, j) + helper(i + 1, m - 1, j + 1, n - 1),
                    helper(0, m - 1, 0, j) + helper(0, i, j + 1, n - 1) + helper(i + 1, m - 1, j + 1, n - 1),
                    helper(0, i, 0, j) + helper(0, i, j + 1, n - 1) + helper(i + 1, m - 1, 0, n - 1),
                    helper(0, i, 0, j) + helper(i + 1, m - 1, 0, j) + helper(0, m - 1, j + 1, n - 1),
                    res,
                )           

        return res
        
