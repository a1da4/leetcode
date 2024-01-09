# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        currDepth = 0
        if not root:
            return currDepth
        nodes = deque([root])
        while nodes:
            currDepth += 1
            N = len(nodes)
            for _ in range(N):
                node = nodes.popleft()
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
        return currDepth
