# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.answer = - float("inf")
        def dfs(root):
            if not root:
                return 0
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            currVal = root.val
            currMax = max(currVal, currVal+leftMax, currVal+rightMax, currVal+leftMax+rightMax)
            self.answer = max(self.answer, currMax)
            return max(currVal, currVal+leftMax, currVal+rightMax)
        
        dfs(root)
        return self.answer
