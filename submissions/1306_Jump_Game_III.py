class Solution:
    def canReach(
        self, 
        arr: List[int], 
        start: int,
    ) -> bool:
        N = len(arr)
        graph = defaultdict(list)
        for i in range(N):
            forward, backward = i + arr[i], i - arr[i]
            if 0 <= forward < N:
                graph[i].append(forward)
            if 0 <= backward < N:
                graph[i].append(backward)
        
        visited = set()
        queue = deque([start])
        goals = set([i for i in range(N) if arr[i] == 0])
        while queue:
            L = len(queue)
            for _ in range(L):
                node = queue.popleft()
                if node in goals:
                    return True
                visited.add(node)

                for neighbour in graph[node]:
                    if neighbour in visited:
                        continue
                    queue.append(neighbour)

        return False
        
