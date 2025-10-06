class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        visited = set()
        heap = []
        heapq.heappush(heap, (grid[0][0], 0, 0))
        visited.add((0, 0))

        while heap:
            t, r, c = heapq.heappop(heap)
            if r == R - 1 and c == C - 1:
                return t
            else:
                for d in [(1,0), (-1,0), (0,1), (0,-1)]:
                    _r, _c = r + d[0], c + d[1]
                    if 0 > _r or R <= _r or 0 > _c or C <= _c:
                        continue
                    if (_r, _c) in visited:
                        continue
                    _t = max(t, grid[_r][_c])
                    heapq.heappush(heap, (_t, _r, _c))
                    visited.add((_r, _c))
