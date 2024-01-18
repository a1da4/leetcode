# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diam = 0
        def calcDepth(node: TreeNode) -> int:
            if node.left:
                left = calcDepth(node.left)
            else:
                left = 0
            if node.right:
                right = calcDepth(node.right)
            else:
                right = 0
            self.diam = max(self.diam, left + right)
            return 1 + max(left, right)

        calcDepth(root)
        return self.diam
