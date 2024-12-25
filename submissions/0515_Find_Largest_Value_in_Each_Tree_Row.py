# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        vals = []
        if not root:
            return vals

        queue = deque([root])
        while queue:
            N = len(queue)
            maxVal = -float("inf")
            for _ in range(N):
                node = queue.popleft()
                maxVal = max(maxVal, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            vals.append(maxVal)
        
        return vals
