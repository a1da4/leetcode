# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        diffheap = []
        queue = deque([root])

        while queue:
            N = len(queue)
            for _ in range(N):
                node = queue.popleft()
                heapq.heappush(diffheap, (abs(node.val - target), node.val))

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return [val for (diff, val) in [heapq.heappop(diffheap) for _ in range(k)]]

