class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        answer = max([max(row) for row in grid])
        R, C = len(grid), len(grid[0])
        visited = [[answer + 1 for _ in range(C)] for _ in range(R)]

        queue = deque([(0, 0, grid[0][0])])

        while queue:
            r, c, t = queue.popleft()
            if r == R - 1 and c == C - 1:
                answer = min(answer, t)
            else:
                for d in [(1,0), (-1,0), (0,1), (0,-1)]:
                    _r, _c = r + d[0], c + d[1]
                    if 0 > _r or R <= _r or 0 > _c or C <= _c:
                        continue
                    _t = max(t, grid[_r][_c])

                    if _t >= visited[_r][_c]:
                        continue
                    
                    visited[_r][_c] = _t
                    queue.append((_r, _c, _t))


        return answer

