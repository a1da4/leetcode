# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        dists = []
        queue = deque([root])
        while queue:
            N = len(queue)
            for _ in range(N):
                node = queue.popleft()
                heapq.heappush(dists, (abs(node.val - target), node.val))
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return heapq.heappop(dists)[1]

