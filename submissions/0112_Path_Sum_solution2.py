# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        queue = [[root, targetSum]]
        while queue:
            node, currentSum = queue.pop(0)
            if not node:
                continue
            if not node.left and not node.right and currentSum == node.val:
                return True

            if node.left:
                queue.append([node.left, currentSum - node.val])
            if node.right:
                queue.append([node.right, currentSum - node.val])

        return False
