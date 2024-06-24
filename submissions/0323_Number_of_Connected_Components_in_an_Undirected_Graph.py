class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.answer = 0
        visited = set()

        graph = defaultdict(list)
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)

        def travel(node: int):
            queue = deque([node])
            while queue:
                N = len(queue)
                for _ in range(N):
                    _node = queue.popleft()
                    if _node in graph:
                        for child in graph[_node]:
                            if child not in visited:
                                visited.add(child)
                                queue.append(child)

        for node in range(n):
            if node in visited:
                continue
            self.answer += 1
            visited.add(node)
            travel(node)

        return self.answer

