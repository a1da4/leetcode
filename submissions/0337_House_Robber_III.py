# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:

        def solver(node: TreeNode) -> List[int]:
            if not node:
                return [0, 0]
            left = solver(node.left)
            right = solver(node.right)
            rob = node.val + left[1] + right[1]

            return [rob, max(left) + max(right)]

        return max(solver(root))

