# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def inorderTraversal(root: Optional[TreeNode]):
            vals = []
            if root:
                vals = inorderTraversal(root.left)
                vals.append(root.val)
                vals = vals + inorderTraversal(root.right)
            return vals
        
        vals = inorderTraversal(root)

        diff = float("inf")
        for i in range(len(vals)-1):
            diff = min(diff, (vals[i+1] - vals[i]))
        return diff
