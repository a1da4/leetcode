class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        answer = [[] for _ in range(n)]

        for edge in edges:
            parent, child = edge
            answer[child].append(parent)
        
        for child in range(n):
            queue = deque(answer[child])
            visited = set(answer[child])
            while queue:
                N = len(queue)
                for _ in range(N):
                    node = queue.popleft()
                    if node not in visited:
                        answer[child].append(node)
                        visited.add(node)
                    nextNodes = answer[node]
                    for _node in nextNodes:
                        if _node not in visited:
                            queue.append(_node)
            answer[child].sort()

        return answer

