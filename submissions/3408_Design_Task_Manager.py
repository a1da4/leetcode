class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.t2u = {}
        self.t2p = {}
        self.heap = []

        for [u, t, p] in tasks:
            self.t2u[t] = u
            self.t2p[t] = p
            heapq.heappush(self.heap, (-p, -t, u))

    def add(
        self, 
        userId: int, 
        taskId: int, 
        priority: int,
    ) -> None:
        self.t2u[taskId] = userId
        self.t2p[taskId] = priority

        heapq.heappush(self.heap, (-priority, -taskId, userId))

    def edit(self, taskId: int, newPriority: int) -> None:
        self.t2p[taskId] = newPriority
        heapq.heappush(
            self.heap, 
            (-newPriority, -taskId, self.t2u[taskId]),
        )

    def rmv(self, taskId: int) -> None:
        self.t2p[taskId] = -1

    def execTop(self) -> int:
        userId = -1
        while self.heap:
            _p, _t, u = heapq.heappop(self.heap)
            p, t = -_p, -_t
            if self.t2p[t] == p and self.t2u[t] == u:
                userId = u
                self.t2p[t] = -1
                break

        return userId
 
