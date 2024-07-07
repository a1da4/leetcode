class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        numRow, numCol = len(grid), len(grid[0])
        buildings = []
        for rowId in range(numRow):
            for colId in range(numCol):
                if grid[rowId][colId] == 1:
                    buildings.append((rowId, colId))
        
        empty2dists = {}
        for rowId in range(numRow):
            for colId in range(numCol):
                if grid[rowId][colId] == 0:
                    empty2dists[(rowId, colId)] = []

        def calculateDistance(building):
            visited = set()
            rowId, colId = building
            queue = deque([(rowId, colId, 0)])
            visited.add((rowId, colId))
            while queue:
                N = len(queue)
                for _ in range(N):
                    x, y, dist = queue.popleft()
                    if grid[x][y] == 0:
                        empty2dists[(x,y)].append(dist)
                    for (dx, dy) in [(1,0), (-1,0), (0,1), (0,-1)]:
                        _x, _y, _dist = x + dx, y + dy, dist + 1
                        if _x < 0 or _x >= numRow:
                            continue
                        if _y < 0 or _y >= numCol:
                            continue
                        if grid[_x][_y] == 1 or grid[_x][_y] == 2:
                            continue
                        if (_x, _y) in visited:
                            continue
                        visited.add((_x, _y))
                        queue.append((_x, _y, _dist))

        minDist = float('inf')
        for building in buildings:
            calculateDistance(building)

        for dists in empty2dists.values():
            if len(dists) == len(buildings):
                dist = sum(dists)
                minDist = min(minDist, dist)

        if minDist == float('inf'):
            return -1
        else:
            return minDist

