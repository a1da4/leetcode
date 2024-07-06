class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        numRow, numCol = len(rooms), len(rooms[0])
        points = deque([])
        for rowId in range(numRow):
            for colId in range(numCol):
                if rooms[rowId][colId] == 0:
                    points.append((rowId, colId, 0))

        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while points:
            N = len(points)
            for _ in range(N):
                rowId, colId, dist = points.popleft()
                for move in moves:
                    _rowId, _colId, _dist = rowId + move[0], colId + move[1], dist + 1
                    if _rowId < 0 or _rowId >= numRow or _colId < 0 or _colId >= numCol:
                        continue
                    roomVal = rooms[_rowId][_colId]
                    if roomVal == 0 or roomVal == -1:
                        continue
                    if roomVal > _dist:
                        rooms[_rowId][_colId] = _dist
                        points.append((_rowId, _colId, _dist))

        return rooms

