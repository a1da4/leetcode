class Solution:
    def __init__(self):
        self.pathBob = {}
        self.visited = []
        self.graph = []

    def travelBob(self, currNode: int, currTime: int) -> True:
        self.pathBob[currNode] = currTime
        self.visited[currNode] = True

        if currNode == 0:
            return True
        
        for adjNode in self.graph[currNode]:
            if not self.visited[adjNode]:
                if self.travelBob(adjNode, currTime + 1):
                    return True
        
        self.pathBob.pop(currNode, None)
        return False

    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        N = len(edges) + 1

        self.graph = [[] for _ in range(N)]
        for edge in edges:
            self.graph[edge[0]].append(edge[1])
            self.graph[edge[1]].append(edge[0])
                
        # calculate B's travel: List[int]
        self.visited = [False] * N
        self.pathBob = {}
        self.travelBob(bob, 0)

        # calculate A's travel: List[int]
        maxScore = -float("inf")
        self.visited = [False] * N
        queue = deque([(0, 0, 0)])
        while queue:
            currNode, currTime, currScore = queue.popleft()
            if (
                currNode not in self.pathBob
                or currTime < self.pathBob[currNode]
            ):
                currScore += amount[currNode]
            elif currTime == self.pathBob[currNode]:
                currScore += amount[currNode] // 2
            else:
                pass

            # isLeaf: update max score of A
            if currNode != 0 and len(self.graph[currNode]) == 1:
                maxScore = max(maxScore, currScore)

            for adjNode in self.graph[currNode]:
                if not self.visited[adjNode]:
                    queue.append((adjNode, currTime + 1, currScore))
            
            self.visited[currNode] = True

        # return max score of A
        return maxScore

