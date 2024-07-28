class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], 
        time: int, change: int) -> int:
        
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        queue = deque([(1, 1)])
        dist1 = [-1] * (n + 1)
        dist2 = [-1] * (n + 1)
        dist1[1] = 0
        while queue:
            node, mode = queue.popleft()
            currTime = dist1[node] if mode == 1 else dist2[node]
            if (currTime // change) % 2:
                currTime = change * (currTime // change + 1)
            currTime += time
        
            for neighbor in graph[node]:
                if dist1[neighbor] == -1:
                    dist1[neighbor] = currTime
                    queue.append((neighbor, 1))
                elif dist2[neighbor] == -1 and dist1[neighbor] != currTime:
                    if neighbor == n:
                        return currTime
                    dist2[neighbor] = currTime
                    queue.append((neighbor, 2))
        
        return 0

