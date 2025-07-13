class Solution:
    def minReorder(
        self, 
        n: int, 
        connections: List[List[int]],
    ) -> int:
        graph = defaultdict(list)
        for connection in connections:
            graph[connection[1]].append((connection[0], 0))
            graph[connection[0]].append((connection[1], 1))
        
        answer = 0
        visited = set()
        queue = deque([0])
        while queue:
            node = queue.popleft()
            visited.add(node)
            for nextNode, isReversed in graph[node]:
                if nextNode in visited:
                    continue
                queue.append(nextNode)
                answer += isReversed
        return answer
