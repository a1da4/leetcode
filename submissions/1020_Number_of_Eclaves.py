class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def move(rId: int, cId: int):
            grid[rId][cId] = 0
            for d in [(1,0), (-1,0), (0,1), (0,-1)]:
                _rId, _cId = rId + d[0], cId + d[1]
                if (0 <= _rId < m
                    and 0 <= _cId < n
                    and grid[_rId][_cId] == 1):
                    move(_rId, _cId)

        for rId in range(m):
            if grid[rId][0] == 1:
                move(rId, 0)
            if grid[rId][n - 1] == 1:
                move(rId, n - 1)

        for cId in range(n):
            if grid[0][cId] == 1:
                move(0, cId)
            if grid[m - 1][cId] == 1:
                move(m - 1, cId)

        return sum([sum(row) for row in grid])

