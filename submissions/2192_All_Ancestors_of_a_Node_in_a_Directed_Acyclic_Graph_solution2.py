class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        neighbors = [[] for _ in range(n)]
        importance = [0] * n
        for edge in edges:
            parent, child = edge
            neighbors[child].append(parent)
            importance[parent] += 1

        queue = deque([nodeId for nodeId in range(n) if importance[nodeId] == 0])

        order = []
        while queue:
            node = queue.popleft()
            order.append(node)

            for _node in neighbors[node]:
                importance[_node] -= 1
                if importance[_node] == 0:
                    queue.append(_node)
        
        order = order[::-1]

        answer = [[] for _ in range(n)]
        answerVocab = [set() for _ in range(n)]

        for child in order:
            for parent in neighbors[child]:
                answerVocab[child].add(parent)
                answerVocab[child].update(answerVocab[parent])

        for nodeId in range(n):
            answer[nodeId].extend(answerVocab[nodeId])
            answer[nodeId].sort()

        return answer

