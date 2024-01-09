# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def getLeaves(root: TreeNode) -> List[int]:
            leaves = []
            def dfs(node: TreeNode):
                if not node.left and not node.right:
                    leaves.append(node.val)
                if node.left:
                    dfs(node.left)
                if node.right:
                    dfs(node.right)
            dfs(root)
            return leaves
        return getLeaves(root1) == getLeaves(root2)
