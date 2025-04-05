class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        answer = 0
        visited = set()

        for node in range(n):
            if node in visited:
                continue
            answer += 1
            queue = deque([node])
            while queue:
                currNode = queue.popleft()
                visited.add(currNode)
                for neighbour in range(n):
                    if (isConnected[currNode][neighbour] == 0
                        or neighbour in visited):
                        continue
                    queue.append(neighbour)

        return answer

