class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n  = len(grid), len(grid[0])
        INF = float("inf")
        minObs = [[INF] * n for _ in range(m)]
        minObs[0][0] = 0

        def is_valid(rId: int, cId: int) -> bool:
            return 0 <= rId < m and 0 <= cId < n

        queue = deque([(0, 0, 0)])
        while queue:
            obs, _rId, _cId = queue.popleft()
            for drId, dcId in dirs:
                rId, cId = _rId + drId, _cId + dcId
                if is_valid(rId, cId) and minObs[rId][cId] == INF:
                    if grid[rId][cId] == 1:
                        minObs[rId][cId] = obs + 1
                        queue.append((obs + 1, rId, cId))
                    else:
                        minObs[rId][cId] = obs
                        queue.appendleft((obs, rId, cId))
        
        return minObs[m - 1][n - 1]

