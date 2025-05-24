class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        visited = set()

        def initialize(r: int, c: int):
            grid[r][c] = -1
            for d in [(1,0), (-1,0), (0,1), (0,-1)]:
                _r, _c = r + d[0], c + d[1]
                if (0 <= _r < R and 0 <= _c < C
                    and grid[_r][_c] == 0):
                    initialize(_r, _c)

        def verify(r: int, c: int) -> bool:
            bools = []
            visited.add((r, c))
            for d in [(1,0), (-1,0), (0,1), (0,-1)]:
                _r, _c = r + d[0], c + d[1]
                if (_r, _c) in visited:
                    bools.append(True)
                    continue
                if 0 > _r or R <= _r or 0 > _c or C <= _c:
                    return False
                
                if grid[_r][_c] == 1:
                    bools.append(True)
                elif grid[_r][_c] == -1:
                    bools.append(False)
                else:
                    bools.append(verify(_r, _c))

            return all(bools)

        for r in range(R):
            if grid[r][0] == 0:
                initialize(r, 0)
            if grid[r][C - 1] == 0:
                initialize(r, C - 1)
        for c in range(C):
            if grid[0][c] == 0:
                initialize(0, c)
            if grid[R - 1][c] == 0:
                initialize(R - 1, c)
    
        answer = 0
        for r in range(R):
            for c in range(C):
                if (grid[r][c] == 0
                    and (r, c) not in visited
                    and verify(r, c)):
                    answer += 1
        
        return answer

