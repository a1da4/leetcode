class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        numRow, numCol = len(maze), len(maze[0])
        rowid2visited = [set() for _ in range (numRow)]

        queue = deque()
        queue.append(start)
        rowid2visited[start[0]].add(start[1])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue:
            curr = queue.popleft()
            if curr[0] == destination[0] and curr[1] == destination[1]:
                return True
        
            for direction in directions:
                rowId, colId = curr
                while 0 <= rowId < numRow and 0 <= colId < numCol and \
                    maze[rowId][colId] == 0:
                    rowId += direction[0]
                    colId += direction[1]
                
                rowId -= direction[0]
                colId -= direction[1]

                if colId not in rowid2visited[rowId]:
                    rowid2visited[rowId].add(colId)
                    queue.append([rowId, colId])

        return False
