class Solution:
    def BFS(
        self,
        nodes: List[Tuple[int]],
        heights: List[List[int]],
    ) -> Set[Tuple[int]]:
        visited = set(nodes)
        queue = deque(nodes)
        while queue:
            r, c = queue.popleft()
            visited.add((r, c))
            for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                _r, _c = r + d[0], c + d[1]
                if (0 <= _r < self.R
                and 0 <= _c < self.C
                and (_r, _c) not in visited
                and heights[r][c] <= heights[_r][_c]):
                    queue.append((_r, _c))
        
        return visited

    def pacificAtlantic(
        self, 
        heights: List[List[int]],
    ) -> List[List[int]]:
        self.R, self.C = len(heights), len(heights[0])

        nodes_p = [(0, 0)] \
            + [(r, 0) for r in range(1, self.R)] \
            + [(0, c) for c in range(1, self.C)] 
        nodes_a = [(self.R - 1, self.C - 1)] \
            + [(r, self.C -1) for r in range(self.R - 1)] \
            + [(self.R - 1, c) for c in range(self.C - 1)]

        visited_p = self.BFS(nodes_p, heights)
        visited_a = self.BFS(nodes_a, heights)
        visited = visited_p & visited_a

        return [[r, c] for r, c in list(visited)]

