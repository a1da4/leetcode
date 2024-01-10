# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = defaultdict(list)
        def dfs(node):
            if node is None:
                return
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        visited = set()
        vals = deque([start])
        time = -1
        while vals:
            time += 1
            N = len(vals)
            for _ in range(N):
                val = vals.popleft()
                visited.add(val)
                for neighbor in graph[val]:
                    if neighbor not in visited:
                        vals.append(neighbor)
        return time
