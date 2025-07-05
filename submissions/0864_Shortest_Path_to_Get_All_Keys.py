class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        visited = set()
        step = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def isLock(dest: str) -> bool:
            return ord("A") <= ord(dest) <= ord("Z")

        def isKey(dest: str) -> bool:
            return ord("a") <= ord(dest) <= ord("z")
        
        def unlocked(dest: str, keyMask: int) -> bool:
            targetKey = 1 << (ord(dest.lower()) - ord('a'))
            return keyMask & targetKey

        R, C = len(grid), len(grid[0])
        def verified(rowId: int, colId: int, keyMask: int) -> bool:
            return (
                0 <= rowId < R and 0 <= colId < C
                and (rowId, colId, keyMask) not in visited
                and grid[rowId][colId] != "#"
            )
        
        for rowId in range(R):
            for colId in range(C):
                if grid[rowId][colId] == "@":
                    queue = deque([(rowId, colId, 0)])
                    visited.add((rowId, colId, 0))
                    break
        numKeys = sum([sum([isKey(cell) for cell in row]) for row in grid])
        allKeys = 0
        for i in range(numKeys):
            allKeys |= 1 << i


        while queue:
            step += 1
            L = len(queue)
            for _ in range(L):
                rowId, colId, keyMask = queue.popleft()
                
                for d in directions:
                    _rowId, _colId = rowId + d[0], colId + d[1]
                    _keyMask = keyMask
                    if not verified(_rowId, _colId, _keyMask):
                        continue
                    dest = grid[_rowId][_colId]
                    if isKey(dest):
                        _keyMask = _keyMask | (1 << (ord(dest) - ord('a')))
                        if _keyMask == allKeys:
                            return step
                    elif isLock(dest):
                        if not unlocked(dest, _keyMask):
                            continue
                    queue.append((_rowId, _colId, _keyMask))
                    visited.add((_rowId, _colId, _keyMask))

        return -1
