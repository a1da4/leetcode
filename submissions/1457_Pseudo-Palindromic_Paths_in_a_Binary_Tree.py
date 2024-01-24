# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self._answer = 0

        def dfs(node: TreeNode, vals: Set[int]):
            if node.val in vals:
                vals.remove(node.val)
            else:
                vals.add(node.val)

            if not node.left and not node.right:
                if len(vals) <= 1:
                    self._answer += 1
                if node.val in vals:
                    vals.remove(node.val)
                else:
                    vals.add(node.val)
                return
            
            if node.left:
                dfs(node.left, vals)
            
            if node.right:
                dfs(node.right, vals)
            
            if node.val in vals:
                vals.remove(node.val)
            else:
                vals.add(node.val)
            
        dfs(root, set())

        return self._answer
