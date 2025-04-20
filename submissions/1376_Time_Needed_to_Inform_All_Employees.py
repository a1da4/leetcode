class Solution:
    def numOfMinutes(
        self, 
        n: int,
        headID: int,
        manager: List[int],
        informTime: List[int],
    ) -> int:
        graph = defaultdict(list)
        for i in range(n):
            if i == headID: continue
            graph[manager[i]].append(i)

        queue = deque([(headID, 0)])
        answer = 0
        while queue:
            L = len(queue)
            for _ in range(L):
                employee, currTime = queue.popleft()
                currTime += informTime[employee]
                answer = max(answer, currTime)
                for subordinate in graph[employee]:
                    queue.append((subordinate, currTime))

        return answer
