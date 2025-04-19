class Solution:
    def shortestAlternatingPaths(
        self, 
        n: int,
        redEdges: List[List[int]], 
        blueEdges: List[List[int]],
    ) -> List[int]:

        graph = defaultdict(list)
        for redEdge in redEdges:
            graph[redEdge[0]].append((redEdge[1], 'r'))
        for blueEdge in blueEdges:
            graph[blueEdge[0]].append((blueEdge[1], 'b'))

        answer = [-1] * n
        queue = deque([(0, 0, None)])
        visited = set()

        while queue:
            L = len(queue)
            for _ in range(L):
                node, step, color = queue.popleft()

                visited.add((node, color))
                if answer[node] == -1:
                    answer[node] = step
                else:
                    answer[node] = min(answer[node], step)

                for nextNode, nextColor in graph[node]:
                    if nextColor == color:
                        continue
                    if (nextNode, nextColor) in visited:
                        continue
                    queue.append((nextNode, step + 1, nextColor))

        return answer

