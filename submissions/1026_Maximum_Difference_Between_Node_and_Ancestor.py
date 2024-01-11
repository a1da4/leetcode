# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        def dfs(node: TreeNode, ancestors: List[int], maxDiff: int):
            maxDiff = max(maxDiff, max([abs(ancestor - node.val) for ancestor in ancestors]))
            if node.left:
                maxDiff = dfs(node.left, ancestors + [node.val], maxDiff)
            if node.right:
                maxDiff = dfs(node.right, ancestors + [node.val], maxDiff)
            return maxDiff

        return dfs(root, [root.val], 0)
