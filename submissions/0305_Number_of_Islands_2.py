class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        answer = []
        grid = [[0 for col in range(n)] for row in range(m)]
        parent = {}
        rank = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    parent[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    parent[rootX] = rootY
                else:
                    parent[rootY] = rootX
                    rank[rootX] += 1

        prev = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for position in positions:
            rowId, colId = position
            if grid[rowId][colId] == 1:
                answer.append(prev)
                continue

            grid[rowId][colId] = 1
            parent[(rowId, colId)] = (rowId, colId)
            rank[(rowId, colId)] = 0
            numAdj = 0

            for d in directions:
                newRow, newCol = rowId + d[0], colId + d[1]
                if 0 <= newRow < m and 0 <= newCol < n and grid[newRow][newCol] == 1:
                    if find((newRow, newCol)) != find((rowId, colId)):
                        union((newRow, newCol), (rowId, colId))
                        numAdj += 1

            prev = prev - numAdj + 1
            answer.append(prev)

        return answer

