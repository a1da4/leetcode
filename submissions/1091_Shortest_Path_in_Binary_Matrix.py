class Solution:
    def shortestPathBinaryMatrix(
        self,
        grid: List[List[int]],
    ) -> int:
        n = len(grid)
        if grid[0][0] or grid[n-1][n-1]:
            return -1
        if n == 1:
            return 1
        dirs = [
            (-1,-1), (-1,0), (-1,1), (0,-1),
            (0,1), (1,-1), (1,0), (1,1)
        ]
        
        q1 = deque([(0, 0)])
        q2 = deque([(n-1, n-1)])
        d1 = {(0, 0): 1}
        d2 = {(n-1, n-1): 1}
        
        while q1 and q2:
            if len(q1) <= len(q2):
                if self.extend(q1, d1, d2, grid, dirs, n):
                    return self.meet_distance(d1, d2)
            else:
                if self.extend(q2, d2, d1, grid, dirs, n):
                    return self.meet_distance(d1, d2)
        return -1
    
    def extend(self, q, dthis, dother, grid, dirs, n):
        for _ in range(len(q)):
            r, c = q.popleft()
            dist = dthis[(r,c)]
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < n 
                    and 0 <= nc < n 
                    and not grid[nr][nc] 
                    and (nr, nc) not in dthis
                ):
                    dthis[(nr,nc)] = dist + 1
                    if (nr, nc) in dother:
                        return True
                    q.append((nr, nc))
        return False
    
    def meet_distance(self, d1, d2):
        return min(
            d1[p] + d2[p] - 1 for p in d1.keys() & d2.keys()
        )

