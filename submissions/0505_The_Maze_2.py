class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        numRow, numCol = len(maze), len(maze[0])
        distances = [[float('inf')] * numCol for _ in range(numRow)]
        distances[start[0]][start[1]] = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        queue = deque([(start[0], start[1])])
        
        while queue:
            x, y = queue.popleft()
            
            for dx, dy in directions:
                nx, ny, dist = x, y, distances[x][y]
                
                while 0 <= nx + dx < numRow and 0 <= ny + dy < numCol and maze[nx + dx][ny + dy] == 0:
                    nx += dx
                    ny += dy
                    dist += 1
                
                if dist < distances[nx][ny]:
                    distances[nx][ny] = dist
                    queue.append((nx, ny))
        
        result = distances[destination[0]][destination[1]]
        return result if result != float('inf') else -1

