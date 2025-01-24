class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        answer = []
        terminals = set()
        queue = deque([(node, path) for node, path in enumerate(graph)])
        prevVisited = set()
        for _ in range(len(graph)):
            visited = set()
            if not queue:
                break
            N = len(queue)
            for _ in range(N):
                node, path = queue.popleft()
                visited.add(node)

                if not path:
                    answer.append(node)
                    terminals.add(node)

                elif path and all([n in terminals for n in path]):
                    answer.append(node)
                    terminals.add(node)
                
                else:
                    queue.append((node, path))
            
            if visited == prevVisited:
                break
            prevVisited = visited

        return sorted(answer)

