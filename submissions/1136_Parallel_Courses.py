class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        requirements = [0] * (n + 1)
        prev2next = defaultdict(list)
        for relation in relations:
            _prev, _next = relation
            prev2next[_prev].append(_next)
            requirements[_next] += 1

        finished = set()
        queue = deque([])
        for node in range(1, n + 1):
            if requirements[node] == 0:
                queue.append(node)
                finished.add(node)

        semesters = 0

        while queue:
            semesters += 1
            N = len(queue)
            for _ in range(N):
                node = queue.popleft()
                for nextNode in prev2next[node]:
                    requirements[nextNode] -= 1
                    if requirements[nextNode] == 0 and nextNode not in finished:
                        queue.append(nextNode)
                        finished.add(nextNode)
        
        if len(finished) == n:
            return semesters
        else:
            return -1


