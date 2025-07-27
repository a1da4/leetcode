class Solution:
    def nearestExit(
        self, 
        maze: List[List[str]], 
        entrance: List[int],
    ) -> int:
        step = 0
        visited = set()
        visited.add((entrance[0], entrance[1]))
        queue = deque([(entrance[0], entrance[1])])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        R, C = len(maze) - 1, len(maze[0]) - 1

        while queue:
            L = len(queue)
            for _ in range(L):
                x, y = queue.popleft()

                for d in directions:
                    _x, _y = x + d[0], y + d[1]

                    if ((_x, _y) in visited 
                    or _x < 0 or _x > R
                    or _y < 0 or _y > C
                    or maze[_x][_y] == "+"):
                        continue

                    if _x == 0 or _y == 0 or _x == R or _y == C:
                        return step + 1
                    
                    queue.append((_x, _y))
                    visited.add((_x, _y))

            step += 1

        return -1

