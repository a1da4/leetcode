# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(
        self, 
        root: TreeNode, 
        target: TreeNode, 
        k: int,
    ) -> List[int]:
        graph = defaultdict(list)
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                queue.append(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                queue.append(node.right)

        answer = []
        queue = deque([target.val])
        visited = set()
        dist = 0
        while queue:
            L = len(queue)
            for _ in range(L):
                node = queue.popleft()
                visited.add(node)
                if dist == k:
                    answer.append(node)
                
                for neighbour in graph[node]:
                    if neighbour in visited:
                        continue
                    queue.append(neighbour)
            
            dist += 1
            if dist > k:
                break

        return answer

