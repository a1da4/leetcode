# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        self.maxAvg = 0
        def dfs(node: Optional[TreeNode]):
            if not node.left and not node.right:
                self.maxAvg = max(self.maxAvg, node.val)
                return [node.val]
            vals = [node.val]
            if node.left:
                vals += dfs(node.left)
            if node.right:
                vals += dfs(node.right)
            self.maxAvg = max(self.maxAvg, sum(vals) / len(vals))

            return vals
        
        dfs(root)
        return self.maxAvg

