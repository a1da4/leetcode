class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        N = len(graph)
        colours = [-1] * N

        for start in range(N):
            queue = deque([start])
            while queue:
                node = queue.popleft()
                for neighbour in graph[node]:
                    if colours[neighbour] == -1:
                        colours[neighbour] = 1 - colours[node]
                        queue.append(neighbour)
                    else:
                        if colours[neighbour] == colours[node]:
                            return False

        return True
