class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        for wall in walls:
            grid[wall[0]][wall[1]] = 2
        
        visited: Set[Tuple[int, int, str]] = set()

        def move(guard: List[int]):
            x, y = guard
            grid[x][y] = 1
            # up
            du = 1
            while x - du >= 0:
                # wall
                if grid[x - du][y] == 2:
                    break
                # visited
                if (x-du, y, "u") in visited:
                    break
                visited.add((x-du, y, "u"))
                grid[x - du][y] = 1
                du += 1
            # down
            dd = 1
            while x + dd < m:
                # wall
                if grid[x + dd][y] == 2:
                    break
                # visited
                if (x+dd, y, "d") in visited:
                    break
                visited.add((x+dd, y, "d"))
                grid[x + dd][y] = 1
                dd += 1
            # right
            dr = 1
            while y + dr < n:
                # wall
                if grid[x][y + dr] == 2:
                    break
                if (x, y+dr, "r") in visited:
                    break
                visited.add((x, y+dr, "r"))
                grid[x][y + dr] = 1
                dr += 1
            # left
            dl = 1
            while y - dl >= 0:
                # wall
                if grid[x][y - dl] == 2:
                    break
                if (x, y-dl, "l") in visited:
                    break
                visited.add((x, y-dl, "l"))
                grid[x][y - dl] = 1
                dl += 1

        for guard in guards:
            move(guard)

        return m * n - sum([sum(row) for row in grid]) + len(walls)

