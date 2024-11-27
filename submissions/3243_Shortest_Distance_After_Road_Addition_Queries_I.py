class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for i in range(n - 1):
            graph[i].append(i + 1)

        def travel(start: int, end: int) -> int:
            queue = deque([start])
            visited = set()
            visited.add(start)
            dist = 0

            while queue:
                N = len(queue)
                for _ in range(N):
                    node = queue.popleft()
                    if node == end:
                        return dist

                    for neighbor in graph[node]:
                        if neighbor in visited:
                            continue
                        queue.append(neighbor)
                        visited.add(neighbor)

                dist += 1

            return -1

        answer = []
        for qs, qe in queries:
            graph[qs].append(qe)
            answer.append(travel(0, n - 1))

        return answer

