class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        parent2child = defaultdict(list)
        for child, parent in zip(pid, ppid):
            parent2child[parent].append(child)
        
        answer = []
        queue = deque([kill])
        while queue:
            N = len(queue)
            for _ in range(N):
                killed = queue.popleft()
                answer.append(killed)
                if len(parent2child[killed]) > 0:
                    for child in parent2child[killed]:
                        queue.append(child)
    
        return answer

