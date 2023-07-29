# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.length = 0

        def dfs(node: Optional[TreeNode], goLeft: bool, steps: int):
            if node:
                self.length = max(self.length, steps)

                if goLeft:
                    dfs(node.left, False, steps+1)
                    dfs(node.right, True, 1)
                else:
                    dfs(node.left, False, 1)
                    dfs(node.right, True, steps+1)
        
        dfs(root, False, 0)
        dfs(root, True, 0)

        return self.length
