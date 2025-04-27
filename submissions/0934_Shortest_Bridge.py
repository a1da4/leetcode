class Solution:
    def shortestBridge(
        self, 
        grid: List[List[int]],
    ) -> int:
        
        n = len(grid)
        visited = [[False]*n for _ in range(n)]
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        q = deque()

        def dfs(r, c):
            if not (0 <= r < n and 0 <= c < n): 
                return
            if visited[r][c] or grid[r][c] == 0: 
                return
            visited[r][c] = True
            q.append((r, c, 0))
            for dr, dc in dirs:
                dfs(r+dr, c+dc)

        # find all points of the 1st island 
        found = False
        for i in range(n):
            if found: 
                break
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    found = True
                    break

        # find closest path to the 2nd island
        while q:
            r, c, level = q.popleft()
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if not (0 <= nr < n and 0 <= nc < n): 
                    continue
                if visited[nr][nc]: 
                    continue
                if grid[nr][nc] == 1:
                    return level
                visited[nr][nc] = True
                q.append((nr, nc, level+1))

        return -1

